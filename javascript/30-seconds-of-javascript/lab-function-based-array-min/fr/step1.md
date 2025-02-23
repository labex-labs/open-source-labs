# Fonction pour renvoyer la valeur minimale d'un tableau

Pour commencer à pratiquer la programmation, ouvrez le Terminal/SSH et tapez `node`.

Cette fonction renvoie la valeur minimale d'un tableau, en se basant sur la fonction fournie.

Pour ce faire, elle utilise `Array.prototype.map()` pour associer chaque élément à la valeur renvoyée par la fonction. Elle utilise ensuite `Math.min()` pour obtenir la valeur minimale.

```js
const minBy = (arr, fn) =>
  Math.min(...arr.map(typeof fn === "function" ? fn : (val) => val[fn]));
```

Vous pouvez utiliser cette fonction en passant un tableau et une fonction. Par exemple :

```js
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], (x) => x.n); // 2
minBy([{ n: 4 }, { n: 2 }, { n: 8 }, { n: 6 }], "n"); // 2
```
