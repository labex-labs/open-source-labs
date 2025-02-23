# Comment filtrer les valeurs non uniques dans un tableau en JavaScript

Pour filtrer les valeurs non uniques dans un tableau en JavaScript, vous pouvez créer un nouveau tableau ne contenant que les valeurs uniques. Voici comment :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez le constructeur `Set` et l'opérateur de propagation (`...`) pour créer un tableau des valeurs uniques dans le tableau original.
3. Utilisez `Array.prototype.filter()` pour créer un tableau ne contenant que les valeurs uniques.

Voici une fonction exemple qui effectue cette opération :

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

Vous pouvez utiliser cette fonction avec n'importe quel tableau pour filtrer les valeurs non uniques. Par exemple :

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
