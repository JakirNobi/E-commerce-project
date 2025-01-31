from django.db import models

# Create your models here.
from django.db import models
CATEGORY_CHOICES =(
    ('EB','Earbuds'),
    ('SW','Smart Watch'),
    ('MS','Mouse'),
    ('SB','Sound Box'),
    ('RT','Router'),
    ('SF','Stand Fan'),
    ('PT','Printer'),
    ('KB','Keyboard'),
    ('HP','Headphone'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    def __str__(self): 
        return self.title