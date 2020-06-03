from django import forms
from .models import HongdaeBoardModel,HongdaeComment

class HongdaeBoardModelForm(forms.ModelForm):
    class Meta:
        model = HongdaeBoardModel
        fields = ['title','body']

class HongdaeCommentForm(forms.ModelForm):
    class Meta:
        model = HongdaeComment
        fields = ['body']