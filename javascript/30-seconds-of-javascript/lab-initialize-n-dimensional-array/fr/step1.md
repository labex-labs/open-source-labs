# Comment initialiser un tableau N-dimensionnel en JavaScript

Pour créer un tableau N-dimensionnel en JavaScript, vous pouvez utiliser la fonction `initializeNDArray`. Cette fonction prend une valeur et un nombre quelconque de dimensions en arguments et renvoie un nouveau tableau initialisé avec cette valeur.

Pour utiliser `initializeNDArray`, vous pouvez suivre ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à coder.
2. Utilisez la récursion pour créer le tableau avec le nombre de dimensions donné.
3. Utilisez `Array.from()` et `Array.prototype.map()` pour générer des lignes où chaque ligne est un nouveau tableau initialisé à l'aide de `initializeNDArray()`.

Voici le code de la fonction `initializeNDArray` :

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

Vous pouvez ensuite appeler `initializeNDArray` avec la valeur et le nombre de dimensions souhaités. Par exemple :

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
