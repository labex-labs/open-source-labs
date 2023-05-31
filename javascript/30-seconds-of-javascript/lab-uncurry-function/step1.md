# Uncurry a Function

To uncurry a function up to a specified depth, use the `uncurry` function.

```js
const uncurry =
  (fn, n = 1) =>
  (...args) => {
    const next = (acc) => (args) => args.reduce((x, y) => x(y), acc);
    if (n > args.length) throw new RangeError("Arguments too few!");
    return next(fn)(args.slice(0, n));
  };
```

To use the `uncurry` function, pass the function you want to uncurry and the depth up to which you want to uncurry it as arguments. The function will return a variadic function that you can call with the arguments you want to pass.

If you don't specify the depth, the function will uncurry up to depth `1`.

```js
const add = (x) => (y) => (z) => x + y + z;
const uncurriedAdd = uncurry(add, 3);
uncurriedAdd(1, 2, 3); // 6
```

If the number of arguments you pass is less than the specified depth, the function will throw a `RangeError`.
