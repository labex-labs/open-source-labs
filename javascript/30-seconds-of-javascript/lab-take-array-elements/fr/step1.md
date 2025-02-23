# Comment supprimer des éléments d'un tableau en JavaScript

Pour supprimer des éléments au début d'un tableau en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal ou SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.slice()` pour créer un nouveau tableau en supprimant `n` éléments au début.
3. Utilisez la fonction `take` dans le extrait de code ci-dessous pour implémenter la logique.

```js
const take = (arr, n = 1) => arr.slice(0, n);
```

Voici un exemple d'utilisation de la fonction `take` :

```js
take([1, 2, 3], 5); // [1, 2, 3]
take([1, 2, 3], 0); // []
```

Dans le premier exemple, `take([1, 2, 3], 5)` renvoie `[1, 2, 3]` car il n'y a que 3 éléments dans le tableau. Dans le second exemple, `take([1, 2, 3], 0)` renvoie `[]` car aucun élément n'est pris au début du tableau.
