from django.urls import path
from . import views

urlpatterns = [
    path('', views.adeverinte_home, name="adeverinte-home"),
    path('about', views.adeverinte_about, name="adeverinte-about"),
]