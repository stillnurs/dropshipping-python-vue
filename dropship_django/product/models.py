from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.enums import TextChoices
from django.core.files import File

from polymorphic.models import PolymorphicModel
from multiselectfield import MultiSelectField

from io import BytesIO
from PIL import Image



def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'



class ImageAlbum(PolymorphicModel):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class ProductImage(PolymorphicModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    thumbnail = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
            return self.name

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



class BaseCategory(PolymorphicModel):
    name = models.CharField(max_length=1000)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Base Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'



class ParentCategory(BaseCategory):
    
    class Meta:
        verbose_name_plural = 'Parent Categories'



class ChildCategory(BaseCategory):
    parent = models.ForeignKey(ParentCategory, related_name='category', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Child Categories'

    def get_absolute_url(self):
                    return f'/{self.parent.slug}/{self.slug}/'



class Category(BaseCategory):
    parent = models.ForeignKey(ChildCategory, related_name='category', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
                    return f'/{self.parent.slug}/{self.slug}/'



class BaseProduct(PolymorphicModel):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE)
    # image = models.ForeignKey(Image, related_name='product_image', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name_plural = 'Base Products'
        
    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return f'/{self.category.slug}/{self.slug}/'



class Product(BaseProduct):

    class Meta:
        verbose_name_plural = 'Products'



class MobilePhone(BaseProduct):
    
    
    CELLULAR_CHOICES = ((1, '5G'),
                        (2, '4G'),
                        (3, 'LTE'),
                        (4, 'GPRS'),
                        (5, 'DUAL-SIM'),
                        )
        
    brand = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    display_size = models.CharField(max_length=255, help_text='Display size in millimeters')
    display_resolution = models.CharField(max_length=255, help_text='Display resolution')
    storage = models.PositiveIntegerField(help_text='phone storage memory size in "GB"')
    ram_memory = models.PositiveIntegerField(help_text='Random Access Memory size in GygaBytes "GB"')
    color = models.CharField(max_length=150)
    cellular = MultiSelectField(choices=CELLULAR_CHOICES, min_choices=1, max_choices=5)
    weight = models.DecimalField(max_digits=10, decimal_places=2, help_text='weight of mobile in gramms')
    size = models.CharField(max_length=150, help_text="Size of device' proportions in millimeters")

    class Meta:
        verbose_name_plural = 'Mobile Phones'

    def __str__(self):
        return self.name
