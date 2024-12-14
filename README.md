# BackEnd MoodMap

[![Python CI Django build and test](https://github.com/Neptune-MIAGE/BackEnd-v2/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/Neptune-MIAGE/BackEnd-v2/actions/workflows/django.yml) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2)
![Latest release](https://img.shields.io/github/v/release/Neptune-MIAGE/BackEnd-v2) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)



[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Neptune-MIAGE_BackEnd-v2&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Neptune-MIAGE_BackEnd-v2)


# Installation du projet

1. Cloner le dépot
2. Se placer a la racine dans le terminal et lancer les commandes suivantes pour créer et lancer l'environnement :
```python
python3 -m venv env # si ça ne fonctionne pas -> python -m venv env

# MacOS & Linux :
source env/bin/activate

# Windows :
env\scripts\activate


# Pour quitter l'environnement il faut faire la commande :
deactivate
```
3. Une fois l'environnement lancé, faire la commande suivante pour installer les dépendances :
```python
pip install -r requirements.txt
```
5. Ensuite, se placer dans /moodapp/ et lancer les commandes suivantes :
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Voila toutes les dépendances installées et le serveur lancé à l'adresse http://127.0.0.1:8000/

# Pour build et accéder la documentation

Depuis la racine du projet en étant dans un (env) :
```
cd website/docs
sphinx-apidoc -o . ..
make html
```
Ensuite pour accéder à la documentation il suffit de se rendre sur :

https://neptune-miage.github.io/BackEnd-v2/

puis "Accès à la documentation"

