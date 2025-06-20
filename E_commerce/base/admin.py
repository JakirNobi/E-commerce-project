from base.models import Category, Product, ProductImage
from django.contrib import admin


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

