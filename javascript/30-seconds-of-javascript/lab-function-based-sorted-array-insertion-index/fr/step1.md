# Fonction pour trouver l'index d'insertion dans un tableau trié

Pour trouver l'index le plus bas pour insérer une valeur dans un tableau et maintenir son ordre de tri, utilisez la fonction `sortedIndexBy(arr, n, fn)` en JavaScript.

Cette fonction vérifie approximativement si le tableau est trié dans l'ordre décroissant puis utilise `Array.prototype.findIndex()` pour trouver l'index approprié en fonction de la fonction itératrice `fn`.

Voici le code de la fonction `sortedIndexBy()` :

```js
const sortedIndexBy = (arr, n, fn) => {
  const isDescending = fn(arr[0]) > fn(arr[arr.length - 1]);
  const val = fn(n);
  const index = arr.findIndex((el) =>
    isDescending ? val >= fn(el) : val <= fn(el)
  );
  return index === -1 ? arr.length : index;
};
```

Vous pouvez appeler la fonction avec un tableau d'objets, une valeur à insérer et une fonction itératrice.

Par exemple, `sortedIndexBy([{ x: 4 }, { x: 5 }], { x: 4 }, o => o.x)` renvoie `0`, qui est l'index où l'objet `{ x: 4 }` devrait être inséré pour maintenir l'ordre de tri basé sur la propriété `x`.
