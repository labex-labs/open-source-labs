# Fonction pour la différence symétrique unique d'un tableau

Pour pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`. La fonction suivante renvoie la différence symétrique unique entre deux tableaux. Elle supprime les valeurs dupliquées de l'un ou l'autre tableau.

Pour y arriver, utilisez `Array.prototype.filter()` et `Array.prototype.includes()` sur chaque tableau pour supprimer les valeurs contenues dans l'autre. Créez un `Set` à partir des résultats pour supprimer les valeurs dupliquées.

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

Utilisez la fonction comme suit :

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
