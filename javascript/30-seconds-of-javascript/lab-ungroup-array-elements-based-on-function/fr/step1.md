# Comment regrouper les éléments d'un tableau en fonction d'une fonction

Si vous avez besoin de regrouper les éléments d'un tableau produit par `zip` et d'appliquer une fonction, vous pouvez utiliser `unzipWith`. Voici comment vous pouvez l'implémenter :

1. Utilisez `Math.max()` et l'opérateur de propagation (`...`) pour obtenir le plus long sous-tableau dans le tableau et `Array.prototype.map()` pour transformer chaque élément en tableau.
2. Utilisez `Array.prototype.reduce()` et `Array.prototype.forEach()` pour mapper les valeurs regroupées dans des tableaux individuels.
3. Utilisez `Array.prototype.map()` et l'opérateur de propagation (`...`) pour appliquer `fn` à chaque groupe individuel d'éléments.

```js
const unzipWith = (arr, fn) =>
  arr
    .reduce(
      (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
      Array.from({
        length: Math.max(...arr.map((x) => x.length))
      }).map((x) => [])
    )
    .map((val) => fn(...val));
```

Pour utiliser `unzipWith`, ouvrez le Terminal/SSH et tapez `node`. Ensuite, vous pouvez exécuter l'exemple suivant :

```js
unzipWith(
  [
    [1, 10, 100],
    [2, 20, 200]
  ],
  (...args) => args.reduce((acc, v) => acc + v, 0)
);
// [3, 30, 300]
```

Cela créera un tableau d'éléments en regroupant les éléments du tableau d'entrée produit par `zip` et en appliquant la fonction fournie.
