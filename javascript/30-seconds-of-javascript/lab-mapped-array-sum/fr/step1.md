# Fonction pour calculer la somme des éléments d'un tableau mappé

Pour calculer la somme d'un tableau en assignant une valeur à chaque élément à l'aide d'une fonction fournie, utilisez la fonction `sumBy`. Cette fonction utilise `Array.prototype.map()` pour assigner à chaque élément la valeur renvoyée par `fn`. Elle utilise ensuite `Array.prototype.reduce()` pour ajouter chaque valeur à un accumulateur, qui est initialisé avec une valeur de `0`.

```js
const sumBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0);
```

Utilisation de l'exemple :

```js
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // Renvoie 20
sumBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // Renvoie 20
```

Pour commencer à pratiquer le codage avec cette fonction, ouvrez le Terminal/SSH et tapez `node`.
