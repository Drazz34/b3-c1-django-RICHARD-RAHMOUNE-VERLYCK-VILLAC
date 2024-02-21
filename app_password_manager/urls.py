from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter_site', views.ajouter_site, name="ajouter_site"),
    path('export_passwords/', views.export_passwords, name='export_passwords'),
    path('import_csv/', views.import_csv, name='import_csv'),
    path('modifier_site/<int:id>/', views.modifier_site, name='modifier_site'),
    path('delete/<int:id>/', views.supprimer_site, name='supprimer_site')

]
