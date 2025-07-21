from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "base"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("all_products/", views.AllProductsView.as_view(), name="all_products"),
    path(
        "all_products/<slug:category_slug>/",
        views.AllProductsView.as_view(),
        name="products_by_category",
    ),
    path(
        "product/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"
    ),
    path("search/", views.SearchView.as_view(), name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
