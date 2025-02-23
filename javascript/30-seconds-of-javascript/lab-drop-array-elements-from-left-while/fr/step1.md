# Suppression d'éléments d'un tableau sur la base d'une fonction

Pour supprimer des éléments spécifiques d'un tableau, utilisez la fonction `dropWhile`, qui supprime les éléments jusqu'à ce que la fonction passée renvoie `true`. La fonction renvoie ensuite les éléments restants du tableau.

Voici comment cela fonctionne :

- Parcourez le tableau en utilisant `Array.prototype.slice()` pour supprimer le premier élément du tableau jusqu'à ce que la valeur renvoyée par `func` soit `true`.
- Retournez les éléments restants.

Exemple d'utilisation :

```js
const dropWhile = (arr, func) => {
  while (arr.length > 0 && !func(arr[0])) arr = arr.slice(1);
  return arr;
};

dropWhile([1, 2, 3, 4], (n) => n >= 3); // [3, 4]
```

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.
