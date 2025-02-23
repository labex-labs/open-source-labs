# Comment calculer la moyenne de nombres en JavaScript

Pour calculer la moyenne de deux nombres ou plus en JavaScript, suivez ces étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez la méthode intégrée `Array.prototype.reduce()` pour ajouter chaque valeur à un accumulateur, initialisé avec une valeur de `0`.
3. Divisez la somme résultante par la longueur du tableau.

Voici un extrait de code exemple que vous pouvez utiliser :

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

Vous pouvez appeler la fonction `average` avec un tableau ou plusieurs arguments :

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
