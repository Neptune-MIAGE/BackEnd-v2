fetch('/moods/user/')
    .then(response => response.json())
    .then(data => {
        console.log("Données récupérées :", data);

        // Préparer les données pour Chart.js
        const labels = data.map(entry => new Date(entry.date).toLocaleDateString()); // Dates
        const moodMapping = { "Happy": 1, "Sad": 2, "Angry": 3 }; // Mapping des humeurs en valeurs numériques
        const moodValues = data.map(entry => moodMapping[entry.mood__name] || 0);

        // Créer le graphique
        const ctx = document.getElementById('testChart').getContext('2d');
        new Chart(ctx, {
            type: 'line', // ou 'bar' pour un histogramme
            data: {
                labels: labels,
                datasets: [{
                    label: 'Humeurs',
                    data: moodValues,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 2,
                    fill: false
                }]
            },
            options: {
                scales: {
                    x: { title: { display: true, text: 'Date' } },
                    y: {
                        title: { display: true, text: 'Humeur' },
                        ticks: {
                            callback: function(value) {
                                // Convertit les valeurs numériques en humeurs
                                return Object.keys(moodMapping).find(key => moodMapping[key] === value) || value;
                            }
                        }
                    }
                }
            }
        });
    })
    .catch(error => console.error("Erreur lors de la récupération des données :", error));
