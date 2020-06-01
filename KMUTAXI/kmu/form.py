from django import forms
from .models import KMU

class KmuForm(forms.ModelForm):
    class Meta:
        model = KMU
        fields = ['title', 'body' ] #원하는 값