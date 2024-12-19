import requests

def reverse_geocode(latitude, longitude):
    """
    Récupère la ville en fonction des coordonnées GPS via l'API Nominatim.
    """
    url = f"https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json",
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("address", {}).get("city", "Inconnue")
    return "Inconnue"
