# Fonctions de convergence

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction `converge` prend une fonction de convergence et une liste de fonctions de branchement en entrée. Elle renvoie une nouvelle fonction qui applique chaque fonction de branchement aux arguments d'entrée. Les résultats des fonctions de branchement sont ensuite passés en tant qu'arguments à la fonction de convergence.

Les méthodes `Array.prototype.map()` et `Function.prototype.apply()` sont utilisées pour appliquer chaque fonction aux arguments d'entrée. L'opérateur de propagation (`...`) est ensuite utilisé pour appeler `converger` avec les résultats de toutes les autres fonctions.

Voici le code pour la fonction `converge` :

```js
const converge =
  (converger, fns) =>
  (...args) =>
    converger(...fns.map((fn) => fn.apply(null, args)));
```

Un exemple d'utilisation de cette fonction est montré ci-dessous. La fonction `average` est créée en appelant `converge` avec une fonction anonyme qui calcule la moyenne d'un tableau. Les fonctions de branchement sont deux fonctions anonymes qui calculent respectivement la somme d'un tableau et sa longueur.

```js
const average = converge(
  (a, b) => a / b,
  [(arr) => arr.reduce((a, v) => a + v, 0), (arr) => arr.length]
);
average([1, 2, 3, 4, 5, 6, 7]); // 4
```

Ce code calcule la moyenne du tableau `[1, 2, 3, 4, 5, 6, 7]` et renvoie `4`.
