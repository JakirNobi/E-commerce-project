from django.shortcuts import render
from django.views import View 
from django.views.generic import ListView, DetailView
from base.models import Product, Category,ProductImage
# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "base/index.html"
    context_object_name = 'products'

class CategoryView(ListView):
    model = Product
    template_name = "base/all_products.html"
    context_object_name = 'all'

class ProductDetailView(DetailView):
    model = Product
    template_name = "base/product.html"
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.object.id)
        return context
