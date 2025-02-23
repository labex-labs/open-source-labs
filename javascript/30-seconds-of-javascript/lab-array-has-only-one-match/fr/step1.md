# Fonction pour vérifier si un tableau a une seule correspondance

Pour vérifier si un tableau a une seule valeur correspondant à la fonction donnée, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.filter()` en combinaison avec `fn` pour trouver tous les éléments du tableau correspondants.
3. Utilisez `Array.prototype.length` pour vérifier si un seul élément correspond à `fn`.

Voici le code :

```js
const hasOne = (arr, fn) => arr.filter(fn).length === 1;
```

Et voici un exemple :

```js
hasOne([1, 2], (x) => x % 2); // true
hasOne([1, 3], (x) => x % 2); // false
```
