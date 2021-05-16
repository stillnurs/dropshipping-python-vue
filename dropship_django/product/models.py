from django.core.files import File
from django.db import models
from django.db.models.fields import TextField
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField

from io import BytesIO
from PIL import Image
import imghdr       # Used to validate images
import urllib3      # Used to download images
import urllib.parse     # Cleans up image urls
import copy         # Copies instances of Image
from io import StringIO    # Used to imitate reading from byte file



class Category(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField()

    class Meta:
        db_table = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, auto_created=True)
    name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'
        # ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def save(self, url='', *args, **kwargs):

        if self.image_link != '' and url != '': # Don't do anything if we don't get passed anything!
            image = self.download_image(url) # See function definition below
            try:
                filename = urllib.parse(url).path.split('/')[-1]
                self.image = filename
                tempfile = image
                tempfile_io = cStringIO.StringIO() # Will make a file-like object in memory that you can then save
                tempfile.save(tempfile_io, format=image.format)
                self.image.save(filename, ContentFile(tempfile_io.getvalue()), save=False) # Set save=False otherwise you will have a looping save method
            except Exception as e:
                print ("Error trying to save model: saving image failed: " + str(e))
                pass
        # We've gotten the image into the ImageField above...now we actually need to save it. 
        # We've redefined the save method for Product, so super *should* get the parent of class Product, 
        # models.Model and then run IT'S save method, which will save the Product like normal

        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name.replace('uploads/',''))

        return thumbnail


    def download_image(self, url=image_link):
        """Downloads an image and makes sure it's verified.

        Returns a PIL Image if the image is valid, otherwise raises an exception.
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'} # More likely to get a response if server thinks you're a browser
        r = urllib3.Request(url, headers=headers)
        request = urllib3.urlopen(r, timeout=10)
        image_data = cStringIO.StringIO(request.read()) # StringIO imitates a file, needed for verification step
        img = Image.open(image_data) # Creates an instance of PIL Image class - PIL does the verification of file
        img_copy = copy.copy(img)   # Verify the copied image, not original - verification requires you to open the image again after verification, 
                                    # but since we don't have the file saved yet we won't be able to. This is because once we read() urllib3.urlopen 
                                    # we can't access the response again without remaking the request (i.e. downloading the image again). Rather than do that, 
                                    # we duplicate the PIL Image in memory.
        if valid_img(img_copy):
            return img
        else:
            # Maybe this is not the best error handling...you might want to just provide a path to a generic image instead
            raise Exception('An invalid image was detected when attempting to save a Product!')


    def valid_img(self, img):
        """Verifies that an instance of a PIL Image Class is actually an image and returns either True or False."""
        type = img.format
        if type in ('GIF', 'JPEG', 'JPG', 'PNG'):
            try:
                img.verify()
                return True
            except:
                return False
        else: return False


    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=)
    image = models.ImageField(null=True, blank=True)

class ProductPrice(models.Model):
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

class ProductColor(models.Model):
    product = models.ForeignKey(Product)
    color = models.URLField(null=True, blank=True)

class ProductStorage(models.Model):
    product = models.ForeignKey(Product)
    storage = models.IntegerField(max_length=6, null=True, blank=True)

    