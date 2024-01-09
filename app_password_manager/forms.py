from django import forms
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['nom', 'url', 'identifiant', 'mot_de_passe']
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'Entrez l\'URL du site'}),
        }