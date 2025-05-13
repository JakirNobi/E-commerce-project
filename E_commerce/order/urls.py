from django.urls import path
from order import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'order'
urlpatterns = [
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.CartView.as_view(),name='cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)