from django.contrib import admin

from .models import Category, Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category', 'slug', 'price', 'image', 'image_link', 'category_id_display')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    raw_id_fields = ('category_id',) 


    def category_id_display(self, obj):
       return obj.category_id
    category_id_display.short_description = 'Category ID'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
