from django.shortcuts import render
from .models import Site


def index(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})


def supprimer_site(request, site_id=None):
    if site_id:
        site = Site.objects.get(pk=int(site_id))
        site.delete()
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})
