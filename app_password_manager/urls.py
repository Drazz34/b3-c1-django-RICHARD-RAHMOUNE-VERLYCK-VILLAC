from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^delete/(?P<site_id>[0-9]+)/$', views.supprimer_site, name='supprimer_site')
]
