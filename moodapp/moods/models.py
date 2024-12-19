from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Modèle utilisateur personnalisé
class CustomUser(AbstractUser):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)  # Facultatif pour conserver la ville
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username

# Modèle Mood
class Mood(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Modèle UserMood
class UserMood(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_moods")
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)  # Définit une date par défaut
    note = models.TextField(null=True, blank=True)  # Note optionnelle
    weather_condition = models.CharField(max_length=100, null=True, blank=True)  # Nouveau champ pour la météo

    def __str__(self):
        return f"{self.user.username} - {self.mood.name} on {self.date}"
