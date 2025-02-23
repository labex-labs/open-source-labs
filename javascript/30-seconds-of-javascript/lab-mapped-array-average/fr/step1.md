# Instructions pour calculer la moyenne d'un tableau mis en correspondance

Pour calculer la moyenne d'un tableau, vous pouvez mapper chaque élément à une nouvelle valeur à l'aide de la fonction fournie. Voici les étapes :

1. Ouvrez le Terminal/SSH et tapez `node` pour commencer à pratiquer la programmation.
2. Utilisez `Array.prototype.map()` pour mapper chaque élément à la valeur renvoyée par `fn`.
3. Utilisez `Array.prototype.reduce()` pour ajouter chaque valeur mise en correspondance à un accumulateur, initialisé avec une valeur de `0`.
4. Divisez le tableau résultant par sa longueur pour obtenir la moyenne.

Voici le code que vous pouvez utiliser :

```js
const averageBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val) => acc + val, 0) / arr.length;
```

Vous pouvez tester cette fonction à l'aide des exemples suivants :

```js
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (o) => o.n); // 5
averageBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 5
```
