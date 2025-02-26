# Portfolio personnel

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants dans votre éditeur.

```txt
├── public
├── src
│   ├── components
│   ├── App.css
│   ├── App.js
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

- Veuillez compléter ce défi dans le fichier `src/App.js`.
- La fonction `toggleVisible` est définie pour vérifier la position de défilement et mettre à jour l'état showBackToTopBtn en conséquence.
- Le hook `useEffect` est utilisé pour ajouter un écouteur d'événements à l'événement de défilement de la fenêtre, qui déclenche la fonction toggleVisible.
- La fonction `scrollToTop` est définie pour faire défiler la fenêtre vers le haut lorsque le bouton retour en haut est cliqué.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Démo du projet terminé](../assets/finished.gif)
