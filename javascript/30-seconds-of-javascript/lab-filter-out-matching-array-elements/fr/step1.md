# Comment filtrer les éléments d'un tableau correspondants en JavaScript

Pour filtrer les éléments dans un tableau JavaScript qui ont une ou plusieurs valeurs spécifiées, suivez ces étapes :

1. Ouvrez le Terminal ou SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.includes()` pour trouver les valeurs à exclure.
3. Utilisez la méthode `Array.prototype.filter()` pour créer un nouveau tableau avec les éléments exclus.

Voici un extrait de code d'exemple :

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

Dans cet exemple, la fonction `without` prend un tableau `arr` et un ou plusieurs arguments `args`. La fonction utilise la méthode `filter()` pour créer un nouveau tableau qui exclut tout élément qui correspond à l'une des valeurs spécifiées dans `args`. La méthode `includes()` est utilisée pour vérifier si la valeur est dans `args`. Enfin, la fonction renvoie le nouveau tableau avec les éléments exclus.
