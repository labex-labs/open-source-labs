# Suppression d'éléments d'un tableau à partir de la droite en fonction d'une fonction

Pour supprimer des éléments de la fin d'un tableau jusqu'à ce qu'une certaine condition soit remplie, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Parcourez le tableau à l'aide de `Array.prototype.slice()` pour supprimer le dernier élément du tableau jusqu'à ce que la `func` passée renvoie `true`.
3. Retournez les éléments restants dans le tableau.

Voici une implémentation d'exemple :

```js
const dropRightWhile = (arr, func) => {
  let rightIndex = arr.length;
  while (rightIndex-- && !func(arr[rightIndex]));
  return arr.slice(0, rightIndex + 1);
};
```

Vous pouvez utiliser cette fonction de la manière suivante :

```js
dropRightWhile([1, 2, 3, 4], (n) => n < 3); // [1, 2]
```
