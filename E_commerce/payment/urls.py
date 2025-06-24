from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'payment'

urlpatterns=[
    path('checkout/',views.CheckoutTemplateView.as_view(),name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

