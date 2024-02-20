
import csv
from django.http import HttpResponse
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

def export_passwords(request):
    sites = Site.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nom', 'URL', 'Identifiant', 'Mot de passe'])
    for site in sites:
        writer.writerow([site.id, site.nom, site.url, site.identifiant, site.mot_de_passe])

    return response

def import_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if csv_file.name.endswith('.csv'):

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.reader(decoded_file)
            for row in csv_reader:

                _, created = Site.objects.get_or_create(
                    nom=row[1],
                    url=row[2],
                    identifiant=row[3],
                    mot_de_passe=row[4]
                )
            return HttpResponse("CSV file imported successfully.")
        else:
            return HttpResponse("File is not a CSV.")
    return render(request, 'index.html')
