from django.shortcuts import render, redirect
from .models import Site
from .forms import SiteForm

def index(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})

def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user  # Associer le site à l'utilisateur connecté
            site.save()
            return redirect('index')
    else:
        form = SiteForm()

    return render(request, 'forms.html', {'form': form})


def supprimer_site(request, site_id=None):
    if site_id:
        site = Site.objects.get(pk=int(site_id))
        site.delete()
    return redirect('index')
