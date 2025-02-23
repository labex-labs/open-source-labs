# Trouver les valeurs uniques dans un tableau avec une fonction

Pour trouver toutes les valeurs uniques d'un tableau, fournissez une fonction de comparaison.

Utilisez `Array.prototype.reduce()` et `Array.prototype.some()` pour créer un tableau ne contenant que la première occurrence unique de chaque valeur. La fonction de comparaison `fn` prend deux arguments, les valeurs des deux éléments en cours de comparaison.

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

Pour tester la fonction, utilisez l'exemple ci-dessous :

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

Commencez à pratiquer la programmation en ouvrant le Terminal/SSH et en tapant `node`.
