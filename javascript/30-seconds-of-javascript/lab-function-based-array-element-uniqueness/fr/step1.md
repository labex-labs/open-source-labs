# Vérification de l'unicité de tous les éléments d'un tableau avec une fonction

Pour vérifier si tous les éléments d'un tableau sont uniques en utilisant une fonction de mappage fournie, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.map()` pour appliquer la fonction `fn` fournie à tous les éléments du tableau `arr`.
3. Créez un nouveau `Set` à partir des valeurs mappées pour ne conserver que les occurrences uniques.
4. Comparez la longueur des valeurs mappées uniques à la longueur du tableau original en utilisant les méthodes `Array.prototype.length` et `Set.prototype.size`.

Voici le code :

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

Vous pouvez utiliser la fonction `allUniqueBy()` pour vérifier si tous les éléments d'un tableau sont uniques. Par exemple :

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
