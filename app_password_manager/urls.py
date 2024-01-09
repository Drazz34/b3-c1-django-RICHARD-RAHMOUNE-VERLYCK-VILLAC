from django.urls import path
from . import views

urlpatterns = [
    path('ajouter_site', views.ajouter_site, name="ajouter_site"),
]