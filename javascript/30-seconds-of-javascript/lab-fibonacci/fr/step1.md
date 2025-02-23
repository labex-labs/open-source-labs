# Suite de Fibonacci

Pour générer la suite de Fibonacci en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node`.
2. Utilisez `Array.from()` pour créer un tableau vide de la longueur spécifique, en initialisant les deux premières valeurs (`0` et `1`).
3. Utilisez `Array.prototype.reduce()` et `Array.prototype.concat()` pour ajouter des valeurs dans le tableau, en utilisant la somme des deux dernières valeurs, sauf pour les deux premières.
4. Appelez la fonction `fibonacci()` et passez la longueur souhaitée de la séquence en tant qu'argument.

Voici le code :

```js
const fibonacci = (n) =>
  Array.from({ length: n }).reduce(
    (acc, val, i) => acc.concat(i > 1 ? acc[i - 1] + acc[i - 2] : i),
    []
  );

fibonacci(6); // [0, 1, 1, 2, 3, 5]
```

Cela générera un tableau contenant la suite de Fibonacci jusqu'au n-ième terme.
