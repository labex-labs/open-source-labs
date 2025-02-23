# Comment supprimer des éléments d'un tableau à partir de la fin en JavaScript

Pour supprimer des éléments de la fin d'un tableau en JavaScript, vous pouvez utiliser la méthode `Array.prototype.slice()`. Voici comment faire :

```js
const takeRight = (arr, n = 1) => arr.slice(arr.length - n, arr.length);
```

Cette fonction crée un nouveau tableau avec les derniers `n` éléments du tableau original. Voici comment l'utiliser :

```js
takeRight([1, 2, 3], 2); // [ 2, 3 ]
takeRight([1, 2, 3]); // [3]
```

Pour utiliser cette fonction, ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
