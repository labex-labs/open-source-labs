# Tic Tac Toe

Pour commencer, ouvrez l'éditeur. Vous pouvez voir les fichiers suivants dans votre éditeur.

```txt
├── public
├── src
│   ├── components
│   │   ├── common
│   │   │   └── Utils.js
│   │   ├── Board.js
│   │   ├── Game.js
│   │   └── Square.js
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── package-lock.json
└── package.json
```

## Exigences

- Pour installer les dépendances du projet, utilisez la commande suivante :

  ```bash
  npm i
  ```

- Veuillez compléter ce défi dans le fichier `src/components/Game.js`.
- Utilisez le hook `useState` pour définir trois variables d'état : board, xTurn et winner.
  - `board` représente l'état du plateau de jeu. Il est initialisé comme un tableau de 9 éléments, où chaque élément est initialement défini sur null.
  - `xTurn` est un drapeau booléen indiquant si c'est actuellement le tour de X.
  - `winner` stocke le résultat de la fonction `calculateWinner`, qui détermine le gagnant en fonction de l'état actuel du plateau.
- La fonction `handleClick` est appelée lorsqu'un carré du plateau de jeu est cliqué.
  - Elle crée une copie de l'état actuel du plateau à l'aide de l'opérateur de propagation (`[...board]`) et l'attribue à tmpBoard.
  - Si un gagnant a déjà été déterminé (winner est vrai) ou si le carré cliqué est déjà marqué (`tmpBoard[i]` est vrai), la fonction retourne sans effectuer aucune modification.
  - Sinon, elle met à jour la valeur du carré cliqué dans `tmpBoard` avec soit "X" soit "O" en fonction de la valeur de `xTurn`.
  - Le `tmpBoard` mis à jour est ensuite défini comme la nouvelle valeur de l'état du plateau à l'aide de `setBoard`, et xTurn est inversé à l'aide de setXTurn.

## Exemple

Une fois que vous avez terminé le code, exécutez-le avec la commande suivante :

```bash
npm start
```

Le résultat final est le suivant :

![Tic Tac Toe game demo](../assets/finished.gif)
