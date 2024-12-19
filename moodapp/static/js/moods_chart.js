console.log("Fichier moods_chart.js chargé !");

document.addEventListener("DOMContentLoaded", () => {
    fetch('/moods/user/') // Récupération des données JSON depuis Django
        .then(response => response.json())
        .then(data => {
            console.log("Données récupérées :", data);

            // Mapping des niveaux d'humeur, couleurs et emojis
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

            const moodEmojis = {
                "Awful": "😡",
                "Sad": "😢",
                "Neutral": "😐",
                "Happy": "😊",
                "Awesome": "😁"
            };

            // Préparation des données pour le graphique
            const labels = data.map(entry => new Date(entry.date).toLocaleDateString());
            const moodValues = data.map(entry => moodMapping[entry.mood__name]);
            const moodColorsList = data.map(entry => moodColors[entry.mood__name]);

            // Création du graphique avec Chart.js
            const ctx = document.getElementById('moodChart');
            if (!ctx) {
                console.error("Impossible de trouver l'élément 'moodChart' !");
                return;
            }

            new Chart(ctx.getContext('2d'), {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Évolution des Humeurs',
                        data: moodValues,
                        borderColor: '#4CAF50', // Couleur par défaut
                        pointBackgroundColor: moodColorsList,
                        pointBorderColor: moodColorsList,
                        pointRadius: 5,
                        pointHoverRadius: 7,
                        segment: {
                            borderColor: (ctx) => {
                                // Utiliser la couleur du point suivant pour le segment
                                const nextIndex = ctx.p1DataIndex;
                                return moodColorsList[nextIndex] || '#4CAF50';
                            }
                        },
                        tension: 0.4, // Ligne courbée
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    // Ajout des emojis dans les tooltips
                                    const moodName = Object.keys(moodMapping).find(key => moodMapping[key] === context.raw);
                                    return `${moodEmojis[moodName]} ${moodName}`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Date' }
                        },
                        y: {
                            title: { display: true, text: 'Niveau d\'Humeur' },
                            ticks: {
                                callback: function(value) {
                                    return Object.keys(moodMapping).find(key => moodMapping[key] === value) || "";
                                }
                            },
                            min: 1, // Awful
                            max: 5  // Awesome
                        }
                    }
                }
            });

            // Génération du compteur d'humeurs
            const moodCounts = data.reduce((acc, entry) => {
                acc[entry.mood__name] = (acc[entry.mood__name] || 0) + 1;
                return acc;
            }, {});

            const moodCounterContainer = document.getElementById('moodCounter');
            if (moodCounterContainer) {
                // Vider le conteneur avant d'ajouter les éléments
                moodCounterContainer.innerHTML = '';
                
                Object.keys(moodCounts).forEach(mood => {
                    const countElement = document.createElement('div');
                    countElement.innerHTML = `
                        <div class="text-center mx-3">
                            <span style="font-size: 2rem;">${moodEmojis[mood]}</span><br>
                            <strong>${moodCounts[mood]}</strong>
                        </div>
                    `;
                    moodCounterContainer.appendChild(countElement);
                });
            }
        })
        .catch(error => console.error("Erreur lors de la récupération des données :", error));
});
