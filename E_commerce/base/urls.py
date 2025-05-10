from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "base"
urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("all_products/",views.AllProductsView.as_view(),name="all_products"),
    path("product/<slug:slug>", views.ProductDetailView.as_view(), name="product_detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
