from django_cron import CronJobBase, Schedule
from .models import CustomUser, Mood, UserMood
from django.utils.timezone import now
import requests


class RecordMoodCronJob(CronJobBase):
    RUN_EVERY_MINS = 720  # Deux fois par jour (12 heures)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'moods.record_mood_cron'  # Identifiant unique

    def do(self):
        print("Début de l'enregistrement des humeurs automatiques.")
        users = CustomUser.objects.all()
        for user in users:
            latitude = user.latitude or 48.8566  # Par défaut Paris
            longitude = user.longitude or 2.3522
            weather_condition = get_weather_condition(latitude, longitude)
            current_hour = now().hour

            # Détermine le moment de la journée
            time_score = 5 if current_hour < 12 else -5

            # Convertit la météo en score
            weather_score = weather_to_score(weather_condition)

            # Calcul du score total
            total_score = weather_score + time_score

            # Détermine l’humeur
            mood = get_mood_from_score(total_score)
            if mood:
                UserMood.objects.create(user=user, mood=mood, note="Enregistrement automatique")
                print(f"Utilisateur : {user.username}, Humeur : {mood.name}, Score : {total_score}, Météo : {weather_condition}")
            else:
                print(f"Échec pour l'utilisateur : {user.username}. Mood introuvable.")
        print("Fin de l'enregistrement des humeurs automatiques.")


def get_weather_condition(latitude, longitude):
    """
    Récupère la condition météo actuelle en fonction des coordonnées.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'current_weather' in data:
                return data['current_weather']['weathercode']  # Retourne le code météo
        print(f"Erreur API Open-Meteo : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'appel API Open-Meteo : {e}")
    return None


def weather_to_score(weather_code):
    # Mapping des codes météo Open-Meteo vers des scores
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
    }
    if weather_code not in weather_score_mapping:
        print(f"Code météo inconnu : {weather_code}")
    return weather_score_mapping.get(weather_code, 0)


def get_mood_from_score(score):
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
    except Mood.DoesNotExist as e:
        print(f"Erreur : {e}")
        return None
