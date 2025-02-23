# Description de l'index d'insertion dernier dans un tableau trié

Pour trouver l'index le plus élevé où une valeur devrait être insérée dans un tableau afin de maintenir son ordre de tri, suivez ces étapes :

- Tout d'abord, vérifiez de manière approximative si le tableau est trié dans l'ordre décroissant.
- Ensuite, utilisez `Array.prototype.reverse()` et `Array.prototype.findIndex()` pour trouver l'index approprié où l'élément devrait être inséré.

Voici le code de la fonction :

```js
const sortedLastIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr
    .reverse()
    .findIndex((el) => (isDescending ? n <= el : n >= el));
  return index === -1 ? 0 : arr.length - index;
};
```

Et voici un exemple d'utilisation de la fonction :

```js
sortedLastIndex([10, 20, 30, 30, 40], 30); // 4
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
