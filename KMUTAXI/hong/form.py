from django import forms
from .models import HongdaeBoardModel

class HongdaeBoardModelForm(forms.ModelForm):
    class Meta:
        model = HongdaeBoardModel
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mytitleclass'}),
            'body': forms.TextInput(attrs={'class': 'mybodyclass'}),
        }

        fields = ['title','body']