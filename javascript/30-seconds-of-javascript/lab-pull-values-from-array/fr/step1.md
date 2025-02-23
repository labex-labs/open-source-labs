# Comment extraire des valeurs d'un tableau en JavaScript

Pour extraire des valeurs spécifiques d'un tableau en JavaScript, vous pouvez utiliser les méthodes `Array.prototype.filter()` et `Array.prototype.includes()`. Voici comment faire :

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

La fonction `pull` prend un tableau et un ou plusieurs arguments qui représentent les valeurs à supprimer. La fonction crée ensuite un nouveau tableau en filtrant les valeurs spécifiées à l'aide de `Array.prototype.filter()`. Elle modifie ensuite le tableau original en réinitialisant sa longueur à `0` et en la remplissant uniquement avec les valeurs extraites à l'aide de `Array.prototype.push()`.

Voici un exemple de manière dont vous pouvez utiliser la fonction `pull` :

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

Dans cet exemple, la fonction `pull` supprime toutes les occurrences de `'a'` et `'c'` du tableau `myArray` et renvoie un nouveau tableau ne contenant que les valeurs `'b'` et `'b'`.
