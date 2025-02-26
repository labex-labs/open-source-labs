# Jeu de compteur

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants à partir de votre éditeur.

```txt
├── public
├── src
│   ├── components
│   │  └── HomePage
│   │       ├── HomePage.css
│   │       └── HomePage.js
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

- Veuillez compléter ce défi dans le fichier `components/HomePage/HomePage.js`.
- Utilisez le hook `useState` pour définir deux variables d'état : `count` et `timer`.
- Utilisez le hook `useEffect` pour démarrer le minuteur lorsque la variable d'état `timer` change.
- Vérifiez la valeur de `timer`. Si elle est égale à zéro, l'effet retourne immédiatement et ne fait rien.
- Si la valeur de `timer` n'est pas zéro, il configure un intervalle qui décrémente la valeur de `timer` de 1 toutes les secondes (1000 millisecondes).
- Retournez une fonction de nettoyage qui annule l'intervalle lorsque le composant est démonté ou lorsque la valeur du minuteur change.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Finished counter game demo](../assets/finished.gif)
