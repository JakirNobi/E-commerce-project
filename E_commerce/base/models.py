from django.db import models

# Create your models here.
from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True, null =True)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering =['-created']
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False,null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category')
    preview_des = models.CharField(max_length=255, verbose_name='Preview Description')
    full_description = models.TextField(max_length=1000, verbose_name='Full Description')
    selling_price = models.FloatField()
    discounted_price = models.FloatField(default=0.0, blank=True,null=True)
    is_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products')

    def __str__(self): 
        return self.name
    class Meta:
        ordering =['-created']
        verbose_name_plural = 'Products'
