# Comment aplatir un tableau avec JavaScript

Pour aplatir un tableau jusqu'à une profondeur spécifiée en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la fonction `flatten` avec deux arguments : `arr` (le tableau à aplatir) et `depth` (le nombre maximum de niveaux imbriqués à aplatir).
3. À l'intérieur de la fonction `flatten`, utilisez la récursion pour décrémenter `depth` de `1` pour chaque niveau de profondeur.
4. Utilisez `Array.prototype.reduce()` et `Array.prototype.concat()` pour fusionner des éléments ou des tableaux.
5. Ajoutez un cas de base pour le moment où `depth` est égal à `1` pour arrêter la récursion.
6. Omettez le second argument, `depth`, pour aplatir seulement jusqu'à une profondeur de `1` (aplatissement unique).

Voici le code pour la fonction `flatten` :

```js
const flatten = (arr, depth = 1) =>
  arr.reduce(
    (a, v) =>
      a.concat(depth > 1 && Array.isArray(v) ? flatten(v, depth - 1) : v),
    []
  );
```

Vous pouvez tester la fonction `flatten` avec les exemples suivants :

```js
flatten([1, [2], 3, 4]); // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2); // [1, 2, 3, [4, 5], 6, 7, 8]
```
