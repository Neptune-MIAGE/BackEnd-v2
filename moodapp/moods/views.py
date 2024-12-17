from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Mood, UserMood
from django.shortcuts import redirect, get_object_or_404


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
        return redirect('user_moods_page')  # Assure-toi que 'user_moods_page' est bien défini dans urls.py

    # Si la méthode n'est pas POST, retourne une erreur
    return JsonResponse({"error": "Méthode non autorisée."}, status=405)

# Vue pour récupérer les humeurs d’un utilisateur

@login_required
def user_moods(request):
    # Récupérer les 10 dernières humeurs triées par date (ordre décroissant) test 
    user_moods = (
        UserMood.objects.filter(user=request.user)
        .order_by('-date')[:10]  # Limiter aux 10 derniers en ordre décroissant
        .values("mood__name", "date")
    )
    # Retourner les données JSON
    return JsonResponse(list(user_moods), safe=False)


@login_required
def user_moods_page(request):
    return render(request, 'moods/user_moods.html')

# exemple ajout vue avec template et envoie d'une variable contenant tout les objets de la classe Classe au template html :
# def vue(request):
#     objet = Classe.objects.all()
#     return render(request, 'moods/sign_in.html', {'objets' : objet })