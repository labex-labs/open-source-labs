# Vérification de l'égalité des éléments d'un tableau avec une fonction donnée

Pour vérifier si tous les éléments d'un tableau sont égaux, utilisez la fonction `allEqualBy`. Cette fonction applique une fonction de mappage donnée `fn` au premier élément du tableau `arr`. Elle vérifie ensuite si `fn` renvoie la même valeur pour tous les éléments du tableau que pour le premier élément, en utilisant `Array.prototype.every()`. La fonction utilise l'opérateur de comparaison stricte, qui ne tient pas compte de l'inégalité de `NaN` avec lui-même.

Voici le code pour `allEqualBy` :

```js
const allEqualBy = (arr, fn) => {
  const eql = fn(arr[0]);
  return arr.every((val) => fn(val) === eql);
};
```

Vous pouvez utiliser `allEqualBy` comme ceci :

```js
allEqualBy([1.1, 1.2, 1.3], Math.round); // true
allEqualBy([1.1, 1.3, 1.6], Math.round); // false
```

Pour commencer à pratiquer la programmation avec cette fonction, ouvrez le Terminal/SSH et tapez `node`.
