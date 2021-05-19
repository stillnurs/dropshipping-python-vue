from django.contrib import admin
from django.db.models import base

from .models import *


class ImageInline(admin.StackedInline):
        model = Image



@admin.register(Store)
class Store(admin.ModelAdmin):
    base_model = Store
    prepopulated_fields = {"slug": ("name",)}
    child_models = (StoreDirectory, ParentCategory, ChildCategory, BaseProductModel)



@admin.register(StoreDirectory)
class StoreDirectoryAdmin(admin.ModelAdmin):
    base_model = StoreDirectory
    prepopulated_fields = {"slug": ("name",)}



@admin.register(ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    base_model = ParentCategory
    prepopulated_fields = {"slug": ("name",)}



@admin.register(ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    base_model = ChildCategory
    prepopulated_fields = {"slug": ("name",)}



@admin.register(BaseProductModel)
class BaseProductAdmin(admin.ModelAdmin):
    base_model = BaseProductModel
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    inlines = (ImageInline,)


    def category_id_display(self, obj):
       return obj.child_category_id
    category_id_display.short_description = 'Category ID'
