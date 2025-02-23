# Fonction pour vérifier si un tableau a plusieurs correspondances

Pour vérifier si un tableau a plus d'une valeur correspondant à une fonction donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.filter()` en combinaison avec `fn` pour trouver tous les éléments du tableau correspondants.
3. Utilisez `Array.prototype.length` pour vérifier s'il y a plus d'un élément correspondant à `fn`.

Voici le code que vous pouvez utiliser :

```js
const hasMany = (arr, fn) => arr.filter(fn).length > 1;
```

Et voici quelques exemples :

```js
hasMany([1, 3], (x) => x % 2); // true
hasMany([1, 2], (x) => x % 2); // false
```
