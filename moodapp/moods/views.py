from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Mood, UserMood
from django.shortcuts import redirect


# Vue pour afficher la liste des humeurs disponibles
@login_required
def list_moods(request):
    moods = Mood.objects.all()  # Récupère tous les moods
    return render(request, 'moods/choose_mood.html', {'moods': moods})

# Vue pour ajouter une humeur pour l'utilisateur connecté
@login_required
def add_user_mood(request):
    if request.method == "POST":
        # Récupère les données du formulaire
        mood_id = request.POST.get("mood_id")
        user = request.user  # Utilisateur connecté

        if user.is_authenticated and mood_id:
            # Crée une nouvelle instance UserMood
            mood = Mood.objects.get(id=mood_id)
            UserMood.objects.create(user=user, mood=mood)
            return redirect('user_moods')  # Redirige vers la liste des moods après soumission

        return JsonResponse({"error": "Utilisateur non authentifié ou mood invalide."}, status=400)

    return JsonResponse({"error": "Méthode non autorisée."}, status=405)

# Vue pour récupérer les humeurs d’un utilisateur
@login_required
def user_moods(request):
    user_moods = UserMood.objects.filter(user=request.user).values("mood__name", "date")
    return JsonResponse(list(user_moods), safe=False)
