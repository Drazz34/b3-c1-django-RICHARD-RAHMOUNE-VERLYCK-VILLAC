
from django.shortcuts import render, redirect
from .forms import SiteForm


def ajouter_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user  # Associer le site à l'utilisateur connecté
            site.save()
            return redirect('nom_de_la_vue_pour_afficher_le_carnet_adresses')
    else:
        form = SiteForm()

    return render(request, 'forms.html', {'form': form})
