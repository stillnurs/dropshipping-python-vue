from django.contrib.auth.models import User
from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(null=True, blank=True, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(help_text='Date Of Birth')
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    class Meta:
        abstract = True



class ShopperProfile(UserModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shoppers')

    class Meta:
        verbose_name_plural = 'Shopper Profiles'
    
    def __str__(self):
        return self.username


class VendorProfile(UserModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendors')
    store_name = models.CharField(max_length=255, null=True, blank=True, unique=True, db_index=True)
    store_address = models.CharField(max_length=255, null=True, blank=True)
    store_dob = models.DateField(null=True, blank=True, help_text='Store date of found')

    class Meta:
        verbose_name_plural = 'Vendor Profiles'

    def __str__(self):
        return self.username

