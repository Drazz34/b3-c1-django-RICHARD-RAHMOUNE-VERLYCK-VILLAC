from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter_site', views.ajouter_site, name="ajouter_site"),
]