# Création d'une application pratique

Maintenant que nous avons une fonction opérationnelle pour calculer la différence entre des dates en secondes, créons une application plus pratique. Nous allons construire un simple minuteur qui calcule le temps écoulé depuis son démarrage.

## Création d'une application de minuteur

Créez un nouveau fichier nommé `timer.js` dans l'IDE Web :

1. Cliquez sur l'icône "Explorer" dans la barre latérale de gauche.
2. Cliquez avec le bouton droit dans l'explorateur de fichiers et sélectionnez "New File".
3. Nommez le fichier `timer.js` et appuyez sur Entrée.
4. Ajoutez le code suivant au fichier :

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Start time - when the script starts running
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// Function to update and display the elapsed time
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Format the time as hours:minutes:seconds
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Clear the console and display the updated time
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// Update the timer every second
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// Keep the script running
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // Run for 1 minute
```

Enregistrez le fichier en appuyant sur Ctrl+S ou en cliquant sur Fichier > Enregistrer.

## Exécution de l'application de minuteur

Pour exécuter l'application de minuteur, utilisez la commande suivante dans le terminal :

```bash
node timer.js
```

Le minuteur démarrera et s'actualisera toutes les secondes, affichant le temps écoulé depuis son démarrage. Le minuteur s'arrêtera automatiquement après 1 minute, ou vous pouvez l'arrêter plus tôt en appuyant sur Ctrl+C.

## Compréhension de l'application de minuteur

Analysons le fonctionnement de l'application de minuteur :

1. Nous définissons la fonction `getSecondsDiffBetweenDates` pour calculer la différence de temps en secondes.
2. Nous enregistrons l'heure de démarrage lorsque le script commence à s'exécuter.
3. Nous définissons une fonction `updateTimer` qui :
   - Récupère l'heure actuelle
   - Calcule le nombre de secondes écoulées depuis l'heure de démarrage
   - Formate le temps écoulé au format heures:minutes:secondes
   - Affiche le temps formaté
4. Nous utilisons `setInterval` pour exécuter la fonction `updateTimer` toutes les 1000 millisecondes (1 seconde).
5. Nous utilisons `setTimeout` pour arrêter le minuteur après 60000 millisecondes (1 minute).

Cette application démontre une utilisation pratique de notre fonction de différence de dates pour créer un minuteur en temps réel.
