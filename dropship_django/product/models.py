from io import BytesIO
from profile.models import VendorProfile

from django.core.files import File
from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import TextChoices
from django.db.models.fields import DateField, related
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from PIL import Image


# Outside function serving pathway for image files
def get_upload_path(instance, filename):
    name = instance.product.name
    slug = slugify(name)
    return "store/%s-%s" % (slug, filename)



class Store(models.Model):
    """
    Store model, used to create stores
    """
    owner = models.ForeignKey(VendorProfile, related_name='stores', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=f'uploads/{name}/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    specifications = models.JSONField(
        verbose_name='Additional Store specifications', blank=True, null=True)

    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return f'/{self.store.slug}/{self.slug}/'



class StoreDirectory(models.Model):
    """
    Base Store Directory class, to create store directory objects
    """
    owner = models.ForeignKey(
        VendorProfile, related_name='store_directories', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='directories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    specifications = models.JSONField(
        verbose_name='Additional Directory specifications', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Base Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.store.slug}/{self.slug}/'




class ParentCategory(models.Model):
    """
    Parent category class, lays under directories
    """
    owner = models.ForeignKey(
        VendorProfile, related_name='parent_categories', on_delete=models.CASCADE)
    directory = models.ForeignKey(
        StoreDirectory, related_name='parent_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    specifications = models.JSONField(
        verbose_name='Additional Parent-category specifications', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Parent Categories'

    def get_absolute_url(self):
        return f'/{self.directory.slug}/{self.slug}/'



class ChildCategory(models.Model):
    """
    Child category class, lowest category
    """
    owner = models.ForeignKey(VendorProfile, related_name='child_categories', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        ParentCategory, related_name='child_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    specifications = models.JSONField(
        verbose_name='Additional Child-category specifications', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Child Categories'

    def get_absolute_url(self):
                    return f'/{self.parent.slug}/{self.slug}/'



class BaseProductModel(models.Model):
    """
    Base Product Model serves as a base model for all product types
    """
    
    class ProductTypes(models.TextChoices):
        PHYSICAL = 'physical', 'PHYSICAL'
        DIGITAL = 'digital', 'DIGITAL'


    # product base relations
    owner = models.ForeignKey(
        VendorProfile, related_name='products', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='store_products', on_delete=models.CASCADE)
    directory = models.ForeignKey(StoreDirectory, related_name='product_directories', on_delete=models.CASCADE)
    parent_category = models.ForeignKey(ParentCategory, related_name='parent_products', on_delete=models.CASCADE)
    child_category = models.ForeignKey(ChildCategory, related_name='child_products', on_delete=models.CASCADE)

    # product specifications
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    
    product_type = models.CharField(
        max_length=8, choices=ProductTypes.choices, default=ProductTypes.PHYSICAL)
    in_stock = models.BooleanField(default=False)
    stock = models.IntegerField(
        default=0, help_text='stock quantity in pcs/packs etc.')
    weight = models.DecimalField(
        max_digits=10, decimal_places=2, help_text='weight of mobile in gramms', blank=True, null=True)
    specifications = models.JSONField(
        verbose_name='additional product specifications', blank=True, null=True)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name_plural = 'Products'
        
    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return f'/{self.parent_category.slug}/\
            {self.child_category}/{self.slug}/'




class Image(models.Model):
    """
    Image class for multiple image uploads for class product
    """

    product = models.ForeignKey(BaseProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path)
    thumbnail = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    default = models.BooleanField(default=False)

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
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
