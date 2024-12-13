from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_moods, name='mood_list'),  # Route principale
    path('add/', views.add_user_mood, name='add_user_mood'),  # Ajouter une humeur
    path('user/<int:user_id>/', views.user_moods, name='user_moods'),  # Humeurs d'un utilisateur
]
