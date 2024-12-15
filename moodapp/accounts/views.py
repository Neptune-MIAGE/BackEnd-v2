from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect

def accounts_home(request):
    return redirect('login')  # Redirige vers la page de connexion
