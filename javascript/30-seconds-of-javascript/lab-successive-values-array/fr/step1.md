# Tableau de valeurs successives

Pour créer un tableau de valeurs successives en JavaScript, vous pouvez utiliser la méthode `Array.prototype.reduce()`. Cette méthode applique une fonction à un accumulateur et à chaque élément du tableau, de gauche à droite, et renvoie un tableau des valeurs réduites successivement.

Voici comment utiliser la fonction `reduceSuccessive` pour appliquer la fonction donnée au tableau donné, en stockant chaque nouveau résultat :

```js
const reduceSuccessive = (arr, fn, acc) =>
  arr.reduce(
    (res, val, i, arr) => (res.push(fn(res.slice(-1)[0], val, i, arr)), res),
    [acc]
  );
```

Vous pouvez ensuite appeler la fonction `reduceSuccessive` avec un tableau, une fonction et une valeur initiale pour l'accumulateur :

```js
reduceSuccessive([1, 2, 3, 4, 5, 6], (acc, val) => acc + val, 0);
// [0, 1, 3, 6, 10, 15, 21]
```

Pour commencer à pratiquer le codage avec cette fonction, ouvrez le Terminal/SSH et tapez `node`.
