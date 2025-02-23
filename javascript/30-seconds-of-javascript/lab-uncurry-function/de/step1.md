# Entkürzen einer Funktion

Um eine Funktion bis zu einer bestimmten Tiefe zu entkürzen, verwenden Sie die `uncurry`-Funktion.

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments too few!");
    return next(fn)(args.slice(0, n));
  };
```

Um die `uncurry`-Funktion zu verwenden, übergeben Sie als Argumente die Funktion, die Sie entkürzen möchten, und die Tiefe, bis zu der Sie sie entkürzen möchten. Die Funktion wird eine variadische Funktion zurückgeben, die Sie mit den Argumenten aufrufen können, die Sie übergeben möchten.

Wenn Sie die Tiefe nicht angeben, wird die Funktion bis zur Tiefe `1` entkürzt.

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

Wenn die Anzahl der übergebenen Argumente kleiner als die angegebene Tiefe ist, wird die Funktion einen `RangeError` werfen.
