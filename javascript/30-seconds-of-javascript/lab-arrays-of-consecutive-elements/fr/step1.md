# Finding Arrays of Consecutive Elements

Pour trouver les tableaux d'éléments consécutifs, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.slice()` pour créer un tableau avec `n - 1` éléments supprimés du début.
3. Utilisez `Array.prototype.map()` et `Array.prototype.slice()` pour mapper chaque élément à un tableau d'`n` éléments consécutifs.

Voici une fonction exemple qui met en œuvre ces étapes :

```js
const findConsecutive = (arr, n) =>
  arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Vous pouvez appeler cette fonction avec un tableau et un nombre `n` pour trouver tous les tableaux d'`n` éléments consécutifs dans le tableau. Par exemple :

```js
findConsecutive([1, 2, 3, 4, 5], 2);
// [[1, 2], [2, 3], [3, 4], [4, 5]]
```
