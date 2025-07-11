# from django.shortcuts import render
# from django.views import View
from django.views.generic import ListView, DetailView
from base.models import Product, Category, ProductImage
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404
# from django.db.models import Count


# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "base/index.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class AllProductsView(ListView):
    model = Product
    template_name = "base/all_products.html"
    context_object_name = "all"
    paginate_by = 8

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            return Product.objects.filter(category=category)
        return Product.objects.filter().order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_count"] = self.get_queryset().count()
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "base/product.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = ProductImage.objects.filter(product=self.object.id)
        return context
