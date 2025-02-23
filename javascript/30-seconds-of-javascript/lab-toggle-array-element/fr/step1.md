# Comment basculer un élément dans un tableau

Pour basculer un élément dans un tableau, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Vérifiez si l'élément donné est dans le tableau à l'aide de `Array.prototype.includes()`.
3. Si l'élément est dans le tableau, utilisez `Array.prototype.filter()` pour le supprimer.
4. Si l'élément n'est pas dans le tableau, utilisez l'opérateur de propagation (`...`) pour l'ajouter.
5. Utilisez la fonction `toggleElement`, qui accepte un tableau et une valeur, pour basculer l'élément dans le tableau.

```js
const toggleElement = (arr, val) =>
  arr.includes(val) ? arr.filter((el) => el !== val) : [...arr, val];

toggleElement([1, 2, 3], 2); // [1, 3]
toggleElement([1, 2, 3], 4); // [1, 2, 3, 4]
```

En suivant ces étapes, vous pouvez facilement basculer un élément dans un tableau à l'aide de JavaScript.
