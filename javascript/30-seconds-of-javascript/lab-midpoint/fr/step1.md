# Instructions for calculating the midpoint between two pairs of (x,y) points:

Pour calculer le point milieu entre deux paires de points (x,y), suivez ces étapes :

1. Extrait les composants du tableau pour obtenir `x1`, `y1`, `x2` et `y2`.
2. Calcule le point milieu pour chaque dimension en divisant la somme des deux extrémités par `2`.

Voici un extrait de code d'exemple qui implémente la fonction de calcul du point milieu :

```js
const midpoint = ([x1, y1], [x2, y2]) => [(x1 + x2) / 2, (y1 + y2) / 2];
```

Vous pouvez appeler la fonction `midpoint` avec les paramètres suivants pour obtenir les coordonnées du point milieu :

```js
midpoint([2, 2], [4, 4]); // [3, 3]
midpoint([4, 4], [6, 6]); // [5, 5]
midpoint([1, 3], [2, 4]); // [1.5, 3.5]
```

# Getting started with coding:

Pour commencer à pratiquer la programmation, suivez ces étapes :

1. Ouvrez le Terminal/SSH.
2. Tapez `node` pour démarrer l'environnement Node.js.
