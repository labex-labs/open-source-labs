# Comment aplatir profondément un tableau en utilisant la récursivité en JavaScript

Pour aplatir profondément un tableau en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la récursivité pour aplatir le tableau.
3. Utilisez la méthode `Array.prototype.concat()` avec un tableau vide (`[]`) et l'opérateur de propagation (`...`) pour aplatir le tableau.
4. Aplatissez de manière récursive chaque élément qui est un tableau.
5. Implémentez le code suivant :

```js
const deepFlatten = (arr) =>
  [].concat(...arr.map((v) => (Array.isArray(v) ? deepFlatten(v) : v)));

deepFlatten([1, [2], [[3], 4], 5]); // [1, 2, 3, 4, 5]
```

En suivant ces étapes, vous pouvez facilement aplatir profondément un tableau en utilisant la récursivité en JavaScript.
