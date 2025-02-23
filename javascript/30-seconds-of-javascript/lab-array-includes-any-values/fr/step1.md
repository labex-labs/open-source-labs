# Vérifier si un tableau contient des valeurs

Pour commencer à pratiquer le codage, ouvrez le Terminal/SSH et tapez `node`.

Pour vérifier si un tableau contient au moins un élément d'un autre tableau, utilisez `Array.prototype.some()` et `Array.prototype.includes()`. Voici une fonction exemple :

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

Vous pouvez appeler cette fonction et passer les deux tableaux que vous voulez comparer en arguments. La fonction retournera une valeur booléenne indiquant si au moins un élément de `values` est inclus dans `arr`. Voici quelques exemples :

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
