from django.http import HttpResponse
from django.shortcuts import render

from django.http import JsonResponse
from .models import Mood, UserMood
from django.views.decorators.http import require_http_methods


# Vue pour afficher la liste des humeurs
@require_http_methods(["GET", "POST"])  # Sensitive
def list_moods(request):
    moods = Mood.objects.all().values("id", "name", "description", "created_at")
    return JsonResponse(list(moods), safe=False)

# Vue pour enregistrer une humeur pour un utilisateur
@require_http_methods(["GET", "POST"])  # Sensitive
def add_user_mood(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        mood_id = request.POST.get("mood_id")
        user_mood = UserMood.objects.create(user_id=user_id, mood_id=mood_id)
        return JsonResponse({"message": "Mood added successfully!", "id": user_mood.id})

# Vue pour afficher les humeurs d’un utilisateur
@require_http_methods(["GET", "POST"])  # Sensitive
def user_moods(request, user_id):
    user_moods = UserMood.objects.filter(user_id=user_id).values("mood__name", "date")
    return JsonResponse(list(user_moods), safe=False)