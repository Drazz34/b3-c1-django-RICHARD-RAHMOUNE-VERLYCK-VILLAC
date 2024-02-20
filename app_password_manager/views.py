from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Site
from .forms import SiteForm
import random
import string


def index(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {'sites': sites})


def ajouter_site(request):
    if request.method == 'GET':
        form = SiteForm()
        return render(request, 'ajouter_site.html', {'form': form})
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            # letters = string.ascii_lowercase
            # form.fields["mot_de_passe"] = ''.join(random.choice(letters) for i in range(10))
            site = form.save(commit=False)
            site.user = request.user  # Associer le site à l'utilisateur connecté
            site.save()
            messages.success(request, 'Le site a bien été ajouté.')
            return redirect('index')
    else:
        messages.error(request, 'Une erreur est survenue.')
        return redirect('index')


def modifier_site(request, id):
    site = get_object_or_404(Site, id=id)

    if request.method == 'GET':
        context = {'form': SiteForm(instance=site), 'id': id}
        return render(request, 'modifier_site.html', context)

    elif request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le site a bien été modifié.')
            return redirect('index')

    else:
        messages.error(request, 'Une erreur est survenue.')
        return redirect('index')


def supprimer_site(request, id):
    site = get_object_or_404(Site, id=id)
    site.delete()
    return redirect('index')
