# Comment trouver l'index d'insertion dans un tableau trié

Pour trouver l'index le plus bas auquel une valeur devrait être insérée dans un tableau trié, suivez ces étapes :

1. Vérifiez si le tableau est trié dans l'ordre décroissant.
2. Utilisez la méthode `Array.prototype.findIndex()` pour trouver l'index approprié où l'élément devrait être inséré.

Voici le code pour implémenter cela :

```js
const sortedIndex = (arr, n) => {
  const isDescending = arr[0] > arr[arr.length - 1];
  const index = arr.findIndex((el) => (isDescending ? n >= el : n <= el));
  return index === -1 ? arr.length : index;
};
```

Vous pouvez appeler la fonction `sortedIndex` en passant le tableau trié et la valeur que vous voulez insérer. Voici quelques exemples :

```js
sortedIndex([5, 3, 2, 1], 4); // Sortie : 1
sortedIndex([30, 50], 40); // Sortie : 1
```

En utilisant cette fonction, vous pouvez facilement trouver l'index d'insertion d'une valeur dans un tableau trié.
