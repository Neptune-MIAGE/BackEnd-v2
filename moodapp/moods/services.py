import requests
from .models import Mood

def get_weather_condition(latitude, longitude):
    """
    Récupère la condition météo actuelle en fonction des coordonnées GPS.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current_weather = data.get('current_weather', {})
            return {
                "weather_code": current_weather.get("weathercode"),
                "temperature": current_weather.get("temperature"),
                "windspeed": current_weather.get("windspeed")
            }
    except Exception as e:
        print(f"Erreur lors de la récupération des données météo : {e}")
    return {"weather_code": None, "temperature": None, "windspeed": None}

def weather_to_score(weather_code):
    """
    Convertit le code météo en score pour calculer l'humeur.
    """
    weather_score_mapping = {
        0: 10,  # Ciel clair
        1: 5,   # Principalement clair
        2: 0,   # Partiellement nuageux
        3: -5,  # Nuageux
        45: -10,  # Brouillard
        48: -10,  # Brouillard givrant
        51: -15,  # Bruine légère
        61: -15,  # Pluie légère
        80: -20,  # Averse de pluie légère
        # Ajoutez d'autres codes si nécessaire
    }
    return weather_score_mapping.get(weather_code, 0)  # Score par défaut : 0

def get_mood_from_score(score):
    """
    Récupère l'humeur correspondante en fonction du score.
    """
    try:
        if score > 15:
            return Mood.objects.get(name="Awesome")
        elif score > 5:
            return Mood.objects.get(name="Happy")
        elif score > -5:
            return Mood.objects.get(name="Neutral")
        elif score > -15:
            return Mood.objects.get(name="Sad")
        else:
            return Mood.objects.get(name="Awful")
    except Mood.DoesNotExist:
        print("Erreur : Mood correspondant introuvable.")
        return None
