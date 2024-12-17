from django.http import HttpResponse
from django.shortcuts import render

from django.http import JsonResponse
from .models import Mood, UserMood
from django.views.decorators.http import require_http_methods


from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST


@require_GET
def list_moods(request):
    moods = Mood.objects.all().values("id", "name", "description", "created_at")
    return JsonResponse(list(moods), safe=False)


@require_POST
def add_user_mood(request):
    user_id = request.POST.get("user_id")
    mood_id = request.POST.get("mood_id")
    if user_id and mood_id:  # Ajout de validation basique
        user_mood = UserMood.objects.create(user_id=user_id, mood_id=mood_id)
        return JsonResponse({"message": "Mood added successfully!", "id": user_mood.id})
    else:
        return JsonResponse({"error": "Missing user_id or mood_id"}, status=400)

@require_GET
def user_moods(request, user_id):
    user_moods = UserMood.objects.filter(user_id=user_id).values("mood__name", "date")
    return JsonResponse(list(user_moods), safe=False)


# exemple ajout vue avec template et envoie d'une variable contenant tout les objets de la classe Classe au template html :
# def vue(request):
#     objet = Classe.objects.all()
#     return render(request, 'moods/sign_in.html', {'objets' : objet })