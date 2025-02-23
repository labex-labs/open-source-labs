# Uncurry une fonction

Pour uncurry une fonction jusqu'à une profondeur spécifiée, utilisez la fonction `uncurry`.

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments trop peu nombreux!");
    return next(fn)(args.slice(0, n));
  };
```

Pour utiliser la fonction `uncurry`, passez la fonction que vous voulez uncurry et la profondeur jusqu'à laquelle vous voulez l'uncurry comme arguments. La fonction retournera une fonction variadique que vous pouvez appeler avec les arguments que vous voulez passer.

Si vous ne spécifiez pas la profondeur, la fonction uncurry jusqu'à la profondeur `1`.

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

Si le nombre d'arguments que vous passez est inférieur à la profondeur spécifiée, la fonction lancera une `RangeError`.
