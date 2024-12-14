from django.urls import path
from . import views

urlpatterns = [
   path('', views.list_moods, name='list_moods'),  # Liste des humeurs disponibles
    path('add/', views.add_user_mood, name='add_user_mood'),  # Ajouter une humeur
     path('user/', views.user_moods, name='user_moods'),  # API pour le JSON
    path('user/page/', views.user_moods_page, name='user_moods_page'),  # Page HTML

]
