# Deshacer el currying de una función

Para deshacer el currying de una función hasta una profundidad especificada, utiliza la función `uncurry`.

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments too few!");
    return next(fn)(args.slice(0, n));
  };
```

Para utilizar la función `uncurry`, pasa la función que quieres deshacer el currying y la profundidad hasta la que la quieres deshacer como argumentos. La función devolverá una función variádica que puedes llamar con los argumentos que quieres pasar.

Si no especificas la profundidad, la función deshacera el currying hasta la profundidad `1`.

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

Si el número de argumentos que pasas es menor que la profundidad especificada, la función lanzará un `RangeError`.
