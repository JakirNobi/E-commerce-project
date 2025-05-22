from django.urls import path
from order import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'order'
urlpatterns = [
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add-to-cart'),
    path('cart_view/',views.cart_view,name='cart'),
    path('remove_item/<int:pk>/',views.remove_item_from_cart,name='remove-item'),
    path('increase_quantity/<int:pk>',views.increase_cart,name='increase'),
    path('decrease_quantity/<int:pk>',views.decrease_cart,name='decrease'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)