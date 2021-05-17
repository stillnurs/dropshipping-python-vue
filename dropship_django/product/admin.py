from django.contrib import admin
from django.db import models
from django.db.models import base
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter, StackedPolymorphicInline, PolymorphicInlineSupportMixin

from .models import BaseCategory, ParentCategory, ChildCategory, Category, BaseProduct, MobilePhone, Image



class ImageInline(admin.StackedInline):
        model = Image



@admin.register(BaseCategory)
class BaseCategoryAdmin(PolymorphicParentModelAdmin):
    base_model = BaseCategory
    prepopulated_fields = {"slug": ("name",)}
    child_models = (ParentCategory, ChildCategory, Category)
    list_filter = (PolymorphicChildModelFilter,)


@admin.register(ParentCategory)
class ParentCategoryAdmin(PolymorphicChildModelAdmin):
    base_model = ParentCategory
    prepopulated_fields = {"slug": ("name",)}



@admin.register(ChildCategory)
class ChildCategoryAdmin(ParentCategoryAdmin):
    base_model = ChildCategory
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Category)
class CategoryAdmin(ChildCategoryAdmin):
    base_model = Category
    prepopulated_fields = {"slug": ("name",)}



@admin.register(BaseProduct)
class BaseProductAdmin(PolymorphicParentModelAdmin):
    base_model = BaseProduct
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    raw_id_fields = ('category_id',) 
    child_models = (MobilePhone,)
    list_filter = (PolymorphicChildModelFilter,)
    

    def category_id_display(self, obj):
       return obj.category_id
    category_id_display.short_description = 'Category ID'



@admin.register(MobilePhone)
class MobilePhoneAdmin(admin.ModelAdmin):
    base_model = MobilePhone
    prepopulated_fields = {"slug": ("name",)}
    inlines = (ImageInline,)


    