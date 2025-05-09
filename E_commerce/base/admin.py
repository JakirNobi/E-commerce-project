from django.contrib import admin
from base.models import Category,Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
# Register your models here.
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)