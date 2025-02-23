# Filtrer les valeurs uniques d'un tableau en fonction d'une fonction

Voici comment créer un tableau qui ne contient que les valeurs non uniques en filtrant les valeurs uniques en fonction d'une fonction de comparaison, `fn` :

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

Pour utiliser cette fonction, appelez `filterUniqueBy()` avec deux arguments : le tableau que vous voulez filtrer et la fonction de comparaison. La fonction de comparaison devrait prendre quatre arguments : les valeurs des deux éléments comparés et leurs index.

Par exemple, si vous avez un tableau d'objets et que vous voulez filtrer les objets avec des valeurs `id` uniques, vous pouvez faire ceci :

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
