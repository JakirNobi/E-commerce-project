from django.shortcuts import render
from django.views import View 
from .models import Product

# Create your views here.
def home(request):
    return render (request,"base/index.html")

class CategoryView(View):
    def get(self,request):
        products =Product.objects.all()
        return render(request,"base/category.html", {"products":products})