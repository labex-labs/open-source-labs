# 反柯里化一个函数

要将一个函数反柯里化到指定深度，请使用 `uncurry` 函数。

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("参数太少！");
    return next(fn)(args.slice(0, n));
  };
```

要使用 `uncurry` 函数，将你想要反柯里化的函数以及你想要反柯里化到的深度作为参数传递。该函数将返回一个可变参数函数，你可以使用想要传递的参数来调用它。

如果你不指定深度，该函数将反柯里化到深度 `1`。

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

如果你传递的参数数量小于指定深度，该函数将抛出一个 `RangeError`。
