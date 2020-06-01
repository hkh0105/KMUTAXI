from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@kookmin.ac.kr" not in data:
            raise forms.ValidationError("국민대 학생이 아닙니다")
        return data

    
