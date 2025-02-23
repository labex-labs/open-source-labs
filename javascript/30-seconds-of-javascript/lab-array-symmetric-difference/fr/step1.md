# Différence symétrique des tableaux

Pour trouver la différence symétrique entre deux tableaux et inclure les valeurs dupliquées, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Créez un `Set` à partir de chaque tableau pour obtenir les valeurs uniques de chacun d'eux.
3. Utilisez `Array.prototype.filter()` sur chacun d'eux pour ne conserver que les valeurs qui ne sont pas contenues dans l'autre.

Voici le code :

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

Vous pouvez utiliser les exemples suivants pour tester la fonction :

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
