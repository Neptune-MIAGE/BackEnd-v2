from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Mood, UserMood
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone  # Utilisez timezone pour garantir la bonne heure
from django.http import JsonResponse
from .models import UserMood


# Vue pour afficher la liste des humeurs disponibles
@login_required
def list_moods(request):
    moods = Mood.objects.all()  # Récupère tous les moods
    return render(request, 'moods/choose_mood.html', {'moods': moods})

# Vue pour ajouter une humeur pour l'utilisateur connecté
@login_required
def add_user_mood(request):
    if request.method == "POST":
        # Récupère l'utilisateur connecté et le mood choisi
        mood_id = request.POST.get("mood_id")
        if mood_id:
            mood = get_object_or_404(Mood, id=mood_id)
            UserMood.objects.create(user=request.user, mood=mood)

        # Redirige directement vers la page du graphique des humeurs après enregistrement
        return redirect('user_moods_page')  
    if request.method == "GET":
        moods = Mood.objects.all()  # Récupère tous les moods
        return render(request, 'moods/choose_mood.html', {'moods': moods})
    # Si la méthode n'est pas POST, retourne une erreur
    return JsonResponse({"error": "Méthode non autorisée."}, status=405)

# Vue pour récupérer les humeurs d’un utilisateur

@login_required
def user_moods(request):
    # Récupérer les 10 derniers humeurs triées par date (ordre croissant)
    user_moods = (
        UserMood.objects.filter(user=request.user)  # Filtrer par utilisateur
        .order_by('date')[:12]  # Tri par date croissante et limiter aux 10 derniers
        .values("mood__name", "date")  # Sélectionner les champs d'intérêt
    )
    
    # Convertir le QuerySet en une liste pour le renvoyer en JSON
    user_moods_list = list(user_moods)
    
    # Retourner les données JSON
    return JsonResponse(user_moods_list, safe=False)


@login_required
def user_moods_page(request):
    return render(request, 'moods/user_moods.html')


def user_moods_json(request):
    user_moods = UserMood.objects.filter(user=request.user).values('date', 'mood__name', 'note')
    return JsonResponse(list(user_moods), safe=False)