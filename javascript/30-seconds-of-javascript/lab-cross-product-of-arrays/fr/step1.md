# Créer un produit croisé d'ensembles en JavaScript

Pour créer un produit croisé d'ensembles en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()`, `Array.prototype.map()` et `Array.prototype.concat()` pour produire chaque paire possible à partir des éléments des deux tableaux.
3. La fonction `xProd()` prend deux tableaux en arguments et crée un nouveau tableau à partir des deux fournis en créant chaque paire possible à partir des tableaux.
4. Voici un exemple de fonctionnement de la fonction `xProd()` :

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

Cela retournera un tableau contenant toutes les paires possibles d'éléments provenant des deux tableaux d'entrée.
