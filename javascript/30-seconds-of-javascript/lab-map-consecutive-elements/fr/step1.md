# Fonction pour mapper des éléments consécutifs dans un tableau

Pour commencer à coder, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction map chaque bloc de `n` éléments consécutifs dans un tableau, en utilisant la fonction `fn` donnée. Suivez ces étapes :

- Utilisez `Array.prototype.slice()` pour obtenir un nouveau tableau `arr` avec les premiers `n` éléments supprimés.
- Utilisez `Array.prototype.map()` et `Array.prototype.slice()` pour appliquer `fn` à chaque bloc de `n` éléments consécutifs dans `arr`.

Voici le code :

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

Par exemple, vous pouvez utiliser `mapConsecutive()` pour mapper chaque bloc de 3 éléments consécutifs dans un tableau de nombres, en les joignant avec des tirets :

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
