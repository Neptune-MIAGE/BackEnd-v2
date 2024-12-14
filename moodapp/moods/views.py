from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Mood, UserMood

# Vue pour afficher la liste des humeurs disponibles
@login_required
def list_moods(request):
    moods = Mood.objects.all()  # Récupère tous les moods
    return render(request, 'moods/choose_mood.html', {'moods': moods})

# Vue pour ajouter une humeur pour l'utilisateur connecté
@login_required
def add_user_mood(request):
    if request.method == "POST":
        mood_id = request.POST.get("mood_id")
        mood = Mood.objects.get(id=mood_id)
        user_mood = UserMood.objects.create(user=request.user, mood=mood)
        return JsonResponse({"message": "Mood added successfully!", "id": user_mood.id})

# Vue pour récupérer les humeurs d’un utilisateur
@login_required
def user_moods(request):
    user_moods = UserMood.objects.filter(user=request.user).values("mood__name", "date")
    return JsonResponse(list(user_moods), safe=False)
