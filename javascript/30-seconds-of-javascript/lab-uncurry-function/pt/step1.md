# _Uncurry_ de uma Função

Para fazer o _uncurry_ de uma função até uma profundidade especificada, use a função `uncurry`.

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments too few!");
    return next(fn)(args.slice(0, n));
  };
```

Para usar a função `uncurry`, passe a função que você deseja fazer o _uncurry_ e a profundidade até a qual você deseja fazê-lo como argumentos. A função retornará uma função variádica que você pode chamar com os argumentos que deseja passar.

Se você não especificar a profundidade, a função fará o _uncurry_ até a profundidade `1`.

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

Se o número de argumentos que você passar for menor que a profundidade especificada, a função lançará um `RangeError`.
