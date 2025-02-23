# Vérifier si tous les éléments d'un tableau sont vrais

Pour vérifier si tous les éléments d'une collection sont `vrai`, vous pouvez utiliser la méthode `Array.prototype.every()`. Cette méthode prend une fonction prédicat en argument et renvoie `vrai` si la fonction évalue à `vrai` pour tous les éléments du tableau.

Pour simplifier le code, vous pouvez utiliser une fonction appelée `all` qui prend un tableau et une fonction prédicat optionnelle en arguments. La fonction utilise `Array.prototype.every()` pour vérifier si tous les éléments du tableau renvoient `vrai` en fonction de la fonction fournie. Si aucune fonction n'est fournie, `Boolean` est utilisé par défaut.

Voici un exemple d'utilisation de la fonction `all` :

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
