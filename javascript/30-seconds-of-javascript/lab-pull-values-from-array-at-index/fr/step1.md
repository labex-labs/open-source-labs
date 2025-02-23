# Comment extraire des valeurs d'un tableau à un index

Pour extraire des valeurs spécifiques d'un tableau à certains index, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.filter()` et `Array.prototype.includes()` pour filtrer les valeurs qui ne sont pas nécessaires et les stocker dans un nouveau tableau appelé `removed`.
3. Définissez `Array.prototype.length` sur `0` pour modifier le tableau original en réinitialisant sa longueur.
4. Utilisez `Array.prototype.push()` pour repopuler le tableau original avec seulement les valeurs extraites.
5. Utilisez `Array.prototype.push()` pour suivre les valeurs supprimées.
6. La fonction `pullAtIndex` prend deux arguments : le tableau original et un tableau d'index à extraire.
7. La fonction renvoie un tableau de valeurs supprimées.

Utilisation exemple :

```js
const pullAtIndex = (arr, pullArr) => {
  let removed = [];
  let pulled = arr
    .map((v, i) => (pullArr.includes(i) ? removed.push(v) : v))
    .filter((v, i) => !pullArr.includes(i));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
  return removed;
};

let myArray = ["a", "b", "c", "d"];
let pulled = pullAtIndex(myArray, [1, 3]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
