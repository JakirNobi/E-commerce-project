from django.contrib import admin
from base.models import Category,Product,ProductImage

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    prepopulated_fields ={'slug':('name',)}


# Register your models here.
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)