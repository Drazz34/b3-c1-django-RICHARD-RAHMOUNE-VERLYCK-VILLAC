from django.shortcuts import render
from .models import Site

def index(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})
