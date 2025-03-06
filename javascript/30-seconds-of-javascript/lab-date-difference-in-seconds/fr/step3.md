# Implémentation de la fonction de différence de dates en utilisant les fonctions fléchées

Maintenant que nous savons comment calculer les différences de dates, implémentons une version plus concise de notre fonction en utilisant les fonctions fléchées.

## Les fonctions fléchées en JavaScript

Les fonctions fléchées offrent une syntaxe plus courte pour écrire des fonctions en JavaScript. Voici comment nous pouvons réécrire notre fonction de différence de dates en utilisant la syntaxe des fonctions fléchées :

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

Cette fonction fait exactement la même chose que notre fonction précédente, mais avec une syntaxe plus propre et plus concise.

## Création d'un fichier JavaScript

Créons un fichier JavaScript pour stocker et tester notre fonction. Quittez l'environnement Node.js en appuyant sur Ctrl+D ou en tapant `.exit` puis en appuyant sur Entrée.

Maintenant, créez un nouveau fichier nommé `dateDifference.js` dans l'IDE Web :

1. Cliquez sur l'icône "Explorer" dans la barre latérale de gauche.
2. Cliquez avec le bouton droit dans l'explorateur de fichiers et sélectionnez "New File".
3. Nommez le fichier `dateDifference.js` et appuyez sur Entrée.
4. Ajoutez le code suivant au fichier :

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Test examples
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Expected output: 2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Expected output: 60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Expected output: 3600
```

Enregistrez le fichier en appuyant sur Ctrl+S ou en cliquant sur Fichier > Enregistrer.

## Exécution du fichier JavaScript

Pour exécuter le fichier que nous venons de créer, utilisez la commande suivante dans le terminal :

```bash
node dateDifference.js
```

Vous devriez voir la sortie suivante :

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

Cela confirme que notre fonction fonctionne correctement :

- Premier exemple : La différence entre 00:00:15 et 00:00:17 est de 2 secondes.
- Deuxième exemple : La différence entre 00:00:00 et 00:01:00 est de 60 secondes (1 minute).
- Troisième exemple : La différence entre 00:00:00 et 01:00:00 est de 3600 secondes (1 heure).
