from django import forms
from .models import HongdaeBoardModel

class HongdaeBoardModelForm(forms.ModelForm):
    class Meta:
        model = HongdaeBoardModel
        fields = ['title','body']