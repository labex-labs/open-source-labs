# Produit cartésien

Pour calculer le produit cartésien de deux tableaux, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()`, `Array.prototype.map()` et l'opérateur de propagation (`...`) pour générer toutes les paires d'éléments possibles à partir des deux tableaux.
3. Utilisez le code suivant :

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

Exemple :

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

Cela générera toutes les combinaisons possibles d'éléments des deux tableaux.
