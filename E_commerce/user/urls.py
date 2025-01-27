# from django.urls import path
# from . import views

# urlpatterns = [
#     path("",views.login),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup_view, name='login_signup'),
    path('logout/', views.logout_view, name='logout'),
]
