from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def accounts_home(request):
    return redirect('login')  # Redirige vers la page de connexion

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l'utilisateur après inscription
            return redirect('add_user_mood')  # Redirige vers une page de ton choix après inscription
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
