# Comment obtenir un échantillonnage pondéré à partir d'un tableau en JavaScript

Pour obtenir aléatoirement un élément d'un tableau en fonction des poids fournis, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.reduce()` pour créer un tableau de sommes partielles pour chaque valeur dans `weights`.
3. Utilisez `Math.random()` pour générer un nombre aléatoire et `Array.prototype.findIndex()` pour trouver l'index correct en fonction du tableau produit précédemment.
4. Enfin, renvoyez l'élément de `arr` avec l'index produit.

Voici le code pour y parvenir :

```js
const weightedSample = (arr, weights) => {
  let roll = Math.random();
  return arr[
    weights
      .reduce(
        (acc, w, i) => (i === 0 ? [w] : [...acc, acc[acc.length - 1] + w]),
        []
      )
      .findIndex((v, i, s) => roll >= (i === 0 ? 0 : s[i - 1]) && roll < v)
  ];
};
```

Vous pouvez tester cette fonction en passant un tableau et ses poids correspondants en arguments :

```js
weightedSample([3, 7, 9, 11], [0.1, 0.2, 0.6, 0.1]); // 9
```
