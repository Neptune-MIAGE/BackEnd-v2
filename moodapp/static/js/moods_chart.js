document.addEventListener("DOMContentLoaded", () => {
    fetch('/moods/user/') // Récupération des données JSON
        .then(response => response.json())
        .then(data => {
            console.log("Données récupérées :", data);

            // Mapping des niveaux d'humeur et couleurs
            const moodMapping = {
                "Awful": 1,
                "Sad": 2,
                "Neutral": 3,
                "Happy": 4,
                "Awesome": 5
            };

            const moodColors = {
                "Awful": '#E53935',     // Rouge
                "Sad": '#FF7043',       // Orange
                "Neutral": '#FFCA28',   // Jaune
                "Happy": '#4CAF50',     // Vert
                "Awesome": '#81C784'    // Vert clair
            };

            // Extraction des données pour le graphique
            const labels = data.map(entry => new Date(entry.date).toLocaleDateString());
            const moodValues = data.map(entry => moodMapping[entry.mood__name]);
            const moodColorsList = data.map(entry => moodColors[entry.mood__name]);

            // Création du graphique
            const ctx = document.getElementById('moodChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Évolution des Humeurs',
                        data: moodValues,
                        borderColor: moodColorsList, // Couleur de la ligne
                        backgroundColor: moodColorsList,
                        pointBackgroundColor: moodColorsList,
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        segment: {
                            borderColor: ctx => {
                                // Changement de couleur au segment suivant
                                const nextIndex = ctx.p1DataIndex;
                                return moodColorsList[nextIndex];
                            }
                        },
                        tension: 0.4, // Ligne lissée
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: true, position: 'top' }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Date' }
                        },
                        y: {
                            title: { display: true, text: 'Niveau d\'Humeur' },
                            ticks: {
                                callback: function(value) {
                                    // Associe les niveaux aux labels des humeurs
                                    return Object.keys(moodMapping).find(key => moodMapping[key] === value) || "";
                                }
                            },
                            min: 1, // Awful en bas
                            max: 5  // Awesome en haut
                        }
                    }
                }
            });
        })
        .catch(error => console.error("Erreur lors de la récupération des données :", error));
});
