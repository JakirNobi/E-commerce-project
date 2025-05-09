from django.shortcuts import render
from django.views import View 
from django.views.generic import ListView, DetailView
from base.models import Product, Category
# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "base/index.html"
    context_object_name = 'products'

class CategoryView(View):
    def get(self,request):
        products =Product.objects.all()
        return render(request,"base/category.html", {"products":products})