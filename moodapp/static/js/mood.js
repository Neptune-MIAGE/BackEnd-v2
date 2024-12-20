// Fonction pour convertir le temps en humeur
function getMoodFromWeather(weatherCode) {
    if (weatherCode === 0) return "Awesome"; // Clear
    if (weatherCode === 1) return "Happy";  // Partially clear
    if (weatherCode === 3) return "Neutral"; // Cloudy
    if (weatherCode === 61) return "Sad";   // Rain
    return "Happy"; // Valeur par défaut
}

// Fonction pour récupérer les données météo d'Open-Meteo
async function fetchWeatherAndSuggestMood() {
    const suggestedMoodDiv = document.getElementById('suggested-mood');

    try {
        // Coordonnées fictives (Paris)
        const latitude = 48.8566;
        const longitude = 2.3522;

        // Requête à Open-Meteo
        const response = await fetch(
            `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
        );
        const data = await response.json();

        // Extraction de la météo actuelle
        const weatherCode = data.current_weather.weathercode; // Exemple de code météo
        const mood = getMoodFromWeather(weatherCode);

        // Affichage de la suggestion d’humeur
        suggestedMoodDiv.textContent = `Suggestion : Basé sur la météo actuelle, nous recommandons l'humeur "${mood}" !`;
        suggestedMoodDiv.classList.remove('d-none');
    } catch (error) {
        console.error("Erreur lors de la récupération des données météo :", error);
        suggestedMoodDiv.textContent = "Impossible de récupérer la météo pour le moment.";
        suggestedMoodDiv.classList.remove('d-none');
    }
}

// Charger la suggestion d'humeur au chargement de la page
document.addEventListener('DOMContentLoaded', fetchWeatherAndSuggestMood);
