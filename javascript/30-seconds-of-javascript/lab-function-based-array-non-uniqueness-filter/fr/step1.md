# Filtrer les valeurs non uniques d'un tableau avec une fonction

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Ce code filtre les valeurs non uniques d'un tableau, en fonction d'une fonction de comparaison fournie. Voici les étapes pour y arriver :

1. Utilisez `Array.prototype.filter()` et `Array.prototype.every()` pour créer un nouveau tableau avec uniquement les valeurs uniques en fonction de la fonction de comparaison `fn`.
2. La fonction de comparaison prend quatre arguments : les valeurs des deux éléments comparés et leurs index.
3. La fonction `filterNonUniqueBy` met en œuvre les étapes ci-dessus et renvoie le tableau des valeurs uniques.

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

Voici un exemple d'utilisation de cette fonction :

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

Ce code est concis, clair et cohérent et devrait fonctionner comme prévu.
