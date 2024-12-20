import os
import django

# Définir le fichier de configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moodapp.settings')

# Initialiser Django
django.setup()

from moods.models import CustomUser, Mood

####################################################################################################

# Crée un utilisateur admin 
if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(username='admin', password='admin', email='admin@example.com')
    print("Superuser 'admin' créé avec le mot de passe 'admin'.")

# Crée un utilisateur standard
if not CustomUser.objects.filter(username='user').exists():
    CustomUser.objects.create_user(username='user', password='user', email='user@example.com')
    print("Utilisateur 'user' créé avec le mot de passe 'user'.")

####################################################################################################

# Crée les moods de base
if not Mood.objects.filter(name='Awesome').exists():
    Mood.objects.create(name='Awesome')
    print("Mood 'Awesome' créé.")

if not Mood.objects.filter(name='Happy').exists():
    Mood.objects.create(name='Happy')
    print("Mood 'Happy' créé.")
    
if not Mood.objects.filter(name='Neutral').exists():
    Mood.objects.create(name='Neutral')
    print("Mood 'Neutral' créé.") 
    
if not Mood.objects.filter(name='Sad').exists():
    Mood.objects.create(name='Sad')
    print("Mood 'Sad' créé.")
    
if not Mood.objects.filter(name='Awful').exists():
    Mood.objects.create(name='Awful')
    print("Mood 'Awful' créé.")
    
####################################################################################################
