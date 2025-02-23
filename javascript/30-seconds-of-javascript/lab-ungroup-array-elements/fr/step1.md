# Comment désagréger les éléments d'un tableau en JavaScript

Pour désagréger les éléments d'un tableau produit par la fonction `zip`, vous pouvez créer un tableau de tableaux à l'aide de la fonction `unzip` en JavaScript. Voici comment :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Math.max()`, `Function.prototype.apply()` pour obtenir le plus long sous-tableau dans le tableau, et `Array.prototype.map()` pour transformer chaque élément en un tableau.
3. Utilisez `Array.prototype.reduce()` et `Array.prototype.forEach()` pour mapper les valeurs groupées sur des tableaux individuels.

Voici le code de la fonction `unzip` :

```js
const unzip = (arr) =>
  arr.reduce(
    (acc, val) => (val.forEach((v, i) => acc[i].push(v)), acc),
    Array.from({
      length: Math.max(...arr.map((x) => x.length))
    }).map((x) => [])
  );
```

Vous pouvez utiliser la fonction `unzip` avec les exemples suivants :

```js
unzip([
  ["a", 1, true],
  ["b", 2, false]
]); // [['a', 'b'], [1, 2], [true, false]]
unzip([
  ["a", 1, true],
  ["b", 2]
]); // [['a', 'b'], [1, 2], [true]]
```

En suivant ces étapes, vous pouvez facilement désagréger les éléments d'un tableau en JavaScript.
