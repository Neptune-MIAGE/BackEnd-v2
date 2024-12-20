from django import forms
from moods.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=False, help_text="Entrez une adresse email valide.")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
