from moods.models import CustomUser
from moods.models import Mood  # Remplace par le nom réel de ton app si nécessaire

# Crée un utilisateur admin
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(username='admin', password='admin', email='admin@example.com')
    print("Superuser 'admin' créé avec le mot de passe 'admin'.")

# Crée les moods de base
if not Mood.objects.filter(name='Sad').exists():
    Mood.objects.create(name='Sad')
    print("Mood 'Sad' créé.")
    
if not Mood.objects.filter(name='Neutral').exists():
    Mood.objects.create(name='Neutral')
    print("Mood 'Neutral' créé.") 

if not Mood.objects.filter(name='Happy').exists():
    Mood.objects.create(name='Happy')
    print("Mood 'Happy' créé.")