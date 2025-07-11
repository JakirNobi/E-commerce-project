from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'payment'

urlpatterns=[
    path('checkout/',views.CheckoutTemplateView.as_view(),name='checkout'),
    path('payment_opts/',views.payment_opts,name = 'payment_opts'),
    path('cod/',views.cash_on_delivery,name='cod'),
    path('sslc/',views.ssl_commerz,name='ssl_commerz'),
    path('sslc/status/',views.sslc_status, name ='status'),
    path('sslc/complete/<val_id>/<tran_id>/',views.sslc_complete, name ='sslc_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

