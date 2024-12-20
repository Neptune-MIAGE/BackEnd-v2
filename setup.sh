#!/bin/bash

# Arrêter le script en cas d'erreur
set -e

# Détection et activation de l'environnement virtuel
if [[ -d "venv" ]]; then
  echo "Activation de l'environnement virtuel..."
  source venv/bin/activate
elif [[ -d "env" ]]; then
  echo "Activation de l'environnement virtuel (env)..."
  source env/bin/activate
else
  echo "⚠️  Aucun environnement virtuel trouvé. Création d'un nouvel environnement virtuel..."
  python3 -m venv env
  source env/bin/activate
  echo "✅ Environnement virtuel créé et activé."
fi

# Installation des dépendances Python
echo "Installation des dépendances Python..."
pip install -r requirements.txt

# Application des migrations
echo "Application des migrations..."
python moodapp/manage.py makemigrations
python moodapp/manage.py migrate

# Initialisation des données de base
echo "Initialisation des données de base..."
python moodapp/manage.py shell < moodapp/initialize_data.py

# Lancement du serveur de développement
echo "Lancement du serveur de développement..."
python moodapp/manage.py runserver
