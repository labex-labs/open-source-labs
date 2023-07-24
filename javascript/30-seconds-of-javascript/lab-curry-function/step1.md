# Currying a Function

To curry a function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion.
3. Check if the number of provided arguments (`args`) is sufficient.
4. If yes, call the passed function `fn`.
5. If not, use `Function.prototype.bind()` to return a curried function `fn` that expects the rest of the arguments.
6. If you want to curry a function that accepts a variable number of arguments (a variadic function, e.g. `Math.min()`), you can optionally pass the number of arguments to the second parameter `arity`.
7. Use the following code:

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

Here are some examples:

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
