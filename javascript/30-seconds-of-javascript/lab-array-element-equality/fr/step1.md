# Vérification de l'égalité des éléments d'un tableau

Pour vérifier si tous les éléments d'un tableau sont identiques, vous pouvez utiliser la méthode `Array.prototype.every()`, qui compare tous les éléments avec le premier.

Voici comment vous pouvez l'implémenter :

```js
const allEqual = (arr) => arr.every((val) => val === arr[0]);
```

Remarque : l'opérateur de comparaison stricte est utilisé pour comparer les éléments. Cet opérateur ne prend pas en compte l'inégalité de `NaN` avec lui-même.

Utilisation de l'exemple :

```js
allEqual([1, 2, 3, 4, 5, 6]); // false
allEqual([1, 1, 1, 1]); // true
```
