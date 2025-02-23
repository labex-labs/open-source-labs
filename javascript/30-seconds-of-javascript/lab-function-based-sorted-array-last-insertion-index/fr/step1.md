# Comment trouver l'index d'insertion dernier dans un tableau trié en fonction d'une fonction

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Voici comment trouver l'index le plus élevé auquel une valeur devrait être insérée dans un tableau pour maintenir son ordre de tri, en fonction d'une fonction itératrice fournie :

1. Vérifiez si le tableau est trié dans l'ordre décroissant.
2. Utilisez `Array.prototype.map()` pour appliquer la fonction itératrice à tous les éléments du tableau.
3. Utilisez `Array.prototype.reverse()` et `Array.prototype.findIndex()` pour trouver l'index approprié où l'élément devrait être inséré, en fonction de la fonction itératrice fournie.

Voyez le code ci-dessous :

```js
const sortedLastIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr
    .map(fn)
    .reverse()
    .findIndex((el) => (isDescending ? val <= el : val >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Voici un exemple :

```js
sortedLastIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, (o) => o.x); // 1
```
