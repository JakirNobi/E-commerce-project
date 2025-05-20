from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category', blank=True, null =True)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering =['-created']
        verbose_name_plural = 'Categories'
    
    def get_category_url(self):
        return reverse('base:category', kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


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
    slug = models.SlugField(unique=True)

    def __str__(self): 
        return self.name
    
    class Meta:
        ordering =['-created']
        verbose_name_plural = 'Products'

    def get_product_url(self):
        return reverse('base:product_detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to='product_gallery')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self): 
        return str(self.product.name)