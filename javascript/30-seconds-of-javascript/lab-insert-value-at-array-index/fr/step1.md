# Comment insérer une valeur à un index spécifique dans un tableau à l'aide de JavaScript

Pour insérer une valeur à un index spécifique dans un tableau à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode `Array.prototype.splice()` avec un index approprié et un compte de suppression de `0`, en étalant les valeurs données à insérer.
3. La fonction `insertAt` prend un tableau, un index et une ou plusieurs valeurs à insérer après l'index spécifié.
4. La fonction modifie le tableau original et renvoie le tableau modifié.

Voici un exemple de la fonction `insertAt` en action :

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

Dans l'exemple ci-dessus, la fonction `insertAt` est utilisée pour insérer la valeur `5` après le deuxième index du tableau `myArray`, et pour insérer les valeurs `4`, `6` et `8` après le premier index du tableau `otherArray`.
