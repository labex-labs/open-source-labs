# Comment trouver la similarité d'ensembles en JavaScript

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. Cela vous aidera à comprendre comment trouver un tableau d'éléments qui apparaissent dans les deux tableaux. Suivez ces étapes :

1. Utilisez la méthode `Array.prototype.includes()` pour déterminer les valeurs qui ne font pas partie de `values`.
2. Utilisez la méthode `Array.prototype.filter()` pour les supprimer.

Voici le code pour trouver la similarité d'ensembles :

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

Vous pouvez tester ce code en exécutant la commande suivante :

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

Cela retournera `[1, 2]` en tant que sortie.
