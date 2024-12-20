:: Arrêter le script en cas d'erreur
@echo off
setlocal enabledelayedexpansion

:: Détection et activation de l'environnement virtuel
if exist "venv\Scripts\activate.bat" (
    echo "Activation de l'environnement virtuel..."
    call "venv\Scripts\activate.bat"
) else if exist "env\Scripts\activate.bat" (
    echo "Activation de l'environnement virtuel (env)..."
    call "env\Scripts\activate.bat"
) else (
    echo "Aucun environnement virtuel trouvé. Création d'un nouvel environnement virtuel..."
    python -m venv env
    call "env\Scripts\activate.bat"
    echo "Environnement virtuel créé et activé."
)

:: Installation des dépendances Python
echo "Installation des dépendances Python..."
pip install -r requirements.txt

:: Application des migrations
echo "Application des migrations..."
python moodapp\manage.py makemigrations
python moodapp\manage.py migrate

:: Initialisation des données de base
echo "Initialisation des données de base..."
python moodapp\initialize_data.py

:: Lancement du serveur de développement
echo "Lancement du serveur de développement..."
python moodapp\manage.py runserver

endlocal
