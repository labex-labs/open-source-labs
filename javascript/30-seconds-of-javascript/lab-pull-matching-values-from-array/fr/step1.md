# Comment extraire des valeurs correspondantes d'un tableau

Pour extraire des valeurs spécifiques d'un tableau à l'aide de JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.filter()` et `Array.prototype.includes()` pour filtrer les valeurs non nécessaires et créer un nouveau tableau.
3. Définissez `Array.prototype.length` pour modifier le tableau original en réinitialisant sa longueur à `0`.
4. Utilisez `Array.prototype.push()` pour repopuler le tableau original avec seulement les valeurs extraites.
5. Utilisez `Array.prototype.push()` pour suivre les valeurs supprimées dans un nouveau tableau.

Voici une fonction d'exemple qui met en œuvre ces étapes :

```js
const pullAtValue = (arr, pullArr) => {
  let removed = [],
    pushToRemove = arr.forEach((v, i) =>
      pullArr.includes(v) ? removed.push(v) : v
    ),
    mutateTo = arr.filter((v, i) => !pullArr.includes(v));
  arr.length = 0;
  mutateTo.forEach((v) => arr.push(v));
  return removed;
};
```

Vous pouvez utiliser cette fonction pour supprimer des valeurs spécifiques d'un tableau et retourner les éléments supprimés comme ceci :

```js
let myArray = ["a", "b", "c", "d"];
let pulled = pullAtValue(myArray, ["b", "d"]);
// myArray = [ 'a', 'c' ], pulled = [ 'b', 'd' ]
```
