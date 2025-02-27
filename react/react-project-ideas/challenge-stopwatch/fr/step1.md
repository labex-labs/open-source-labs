# Montre à stop

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants à partir de votre éditeur.

```txt
├── public
├── src
│   ├── components
│   │   ├──common
│   │   ├── stopwatch
│   │   ├── timer
│   │   ├── App.css
│   │   └── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Exigences

- Pour installer les dépendances du projet, utilisez la commande suivante :

  ```bash
  npm i
  ```

- Veuillez compléter ce défi dans le fichier `src/components/timer/Timer.js`.
- La fonction `onStart` est appelée toutes les secondes par le hook useEffect.
  - Elle vérifie si le minuteur est arrivé à 0 heures, 0 minutes et 0 secondes. Dans ce cas, elle définit isStarted sur false et renvoie.
  - Si le minuteur n'est pas démarré, elle renvoie sans effectuer aucune modification.
  - Si le minuteur est en cours d'exécution, elle décrémente le minuteur de 1 seconde.
  - Si les minutes ou les secondes atteignent 0, elle ajuste les heures, les minutes ou les secondes en conséquence en utilisant la fonction setTimer.
- La fonction `onReset` est appelée lorsque le bouton "Réinitialiser" est cliqué.
  - Elle définit isStarted sur false et remet le minuteur à 0 heures, 0 minutes et 0 secondes.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Démonstration de montre à stop terminée](../assets/finished.gif)
