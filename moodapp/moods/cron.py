from .models import DynamicMood
from .services import get_weather_condition, calculate_mood_score, determine_mood_from_score
from django.utils.timezone import now

def generate_dynamic_mood(user):
    # Détermine le contexte matin/soir
    current_hour = now().hour
    context = "morning" if current_hour < 12 else "evening"

    # Récupère la météo actuelle
    weather = get_weather_condition()

    # Calcule le score
    score = calculate_mood_score(context, weather)

    # Détermine l'humeur
    mood = determine_mood_from_score(score)

    # Enregistre l'humeur dynamique
    DynamicMood.objects.create(
        user=user,
        mood_type=mood,
        weather_condition=weather,
        score=score
    )
