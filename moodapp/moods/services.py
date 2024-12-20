import requests
from datetime import datetime

def get_weather_condition():
    # API météo pour récupérer les conditions météo actuelles
    API_KEY = "VOTRE_CLÉ_API"
    CITY = "Paris"  # Changez selon vos besoins
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']  # Exemple : "Rain", "Clear", "Clouds"
        return weather
    return "Unknown"

def calculate_mood_score(context, weather):
    """
    Calcule un score basé sur le contexte (matin/soir) et la météo.
    """
    context_scores = {"morning": 5, "evening": -5}
    weather_scores = {
        "Clear": 10,    # Ensoleillé
        "Rain": -15,    # Pluie
        "Clouds": 0,    # Nuageux
        "Snow": -10,    # Neige
        "Unknown": 0    # Par défaut
    }

    context_score = context_scores.get(context, 0)
    weather_score = weather_scores.get(weather, 0)

    return context_score + weather_score

def determine_mood_from_score(score):
    """
    Détermine une humeur basée sur le score.
    """
    if score >= 15:
        return "Awesome"
    elif score >= 5:
        return "Happy"
    elif score >= -5:
        return "Neutral"
    elif score >= -15:
        return "Sad"
    else:
        return "Awful"
