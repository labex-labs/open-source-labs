# Comment filtrer les valeurs uniques dans un tableau à l'aide de JavaScript

Pour filtrer les valeurs uniques dans un tableau à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer le codage.
2. Utilisez le constructeur `Set` et l'opérateur de propagation (`...`) pour créer un tableau des valeurs uniques de votre tableau original.
3. Utilisez `Array.prototype.filter()` pour créer un tableau ne contenant que les valeurs non uniques.
4. Définissez une fonction appelée `filterUnique` qui prend un tableau en argument et applique les étapes ci-dessus à celui-ci.
5. Appelez la fonction `filterUnique` avec votre tableau en argument.

Voici un extrait de code d'exemple pour y parvenir :

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

Dans l'extrait de code ci-dessus, la fonction `filterUnique` prend un tableau et applique le constructeur `Set` et la méthode `Array.prototype.filter()` à celui-ci pour renvoyer un tableau ne contenant que les valeurs non uniques.
