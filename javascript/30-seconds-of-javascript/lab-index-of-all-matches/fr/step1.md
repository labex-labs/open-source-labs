# Tous les index de correspondance

Pour trouver tous les index de `val` dans un tableau, utilisez `Array.prototype.reduce()` pour parcourir les éléments et stocker les index des éléments correspondants. Si `val` n'apparaît jamais, un tableau vide est renvoyé.

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

Utilisation exemple :

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Ceci est un index de toutes les correspondances.
