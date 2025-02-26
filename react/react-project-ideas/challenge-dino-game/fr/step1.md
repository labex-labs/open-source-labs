# Jeu de dinosaure

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants depuis votre éditeur.

```txt
├── public
├── src
│   ├──components
│   │  └── Dino
│   │       ├── img
│   │       │   ├── cactus.png
│   │       │   └── trex.png
│   │       ├── Dino.css
│   │       └── Dino.js
│   ├── App.js
│   ├── App.css
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

- Veuillez compléter ce défi dans le fichier `src/components/Dino/Dino.js`.
- Initialisez deux hooks `useRef` : `dinoRef` et `cactusRef`. Ces hooks seront utilisés pour référencer les éléments DOM du dinosaure et du cactus.
- Initialisez un hook `useState` appelé score avec une valeur initiale de 0. Ce hook suivra le score du joueur.
- Définissez la fonction jump. Elle ajoute la classe "jump" à l'élément DOM du dinosaure référencé par dinoRef. Cela déclenche une animation CSS qui fait sauter le dinosaure. Après un délai de 300 millisecondes, la classe "jump" est supprimée, ramenant le dinosaure à sa position initiale.
- Utilisez le hook `useEffect` pour gérer la logique du jeu. Il configure un intervalle qui s'exécute toutes les 10 millisecondes. Dans la fonction d'intervalle, il récupère la position actuelle du dinosaure (dinoTop) et du cactus (cactusLeft) en utilisant la fonction getComputedStyle.
- Il vérifie s'une collision s'est produite en comparant la position du cactus (cactusLeft) avec la position du dinosaure (dinoTop). Si le cactus est dans une certaine plage et à la même hauteur que le dinosaure, une collision est détectée. Dans ce cas, une alerte est affichée avec le score du joueur, et le score est réinitialisé à 0 en utilisant la fonction setScore. Sinon, le score est incrémenté de 1 en utilisant setScore.
- Le premier hook `useEffect` renvoie également une fonction de nettoyage qui supprime l'intervalle lorsque le composant est démonté. Cela garantit que l'intervalle est correctement nettoyé pour éviter les fuites mémoire.
- Le second hook `useEffect` est responsable de la configuration et de la suppression d'un écouteur d'événements pour l'événement "keydown". Lorsqu'une touche est pressée, la fonction jump est appelée. Cela permet au joueur de faire sauter le dinosaure en appuyant sur n'importe quelle touche.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Résultat final du jeu de dinosaure](../assets/finished.gif)
