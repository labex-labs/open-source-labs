# Function Composition with Pipes

To start practicing coding with pipes, open the Terminal/SSH and type `node`.

The `pipeFunctions` function performs left-to-right function composition using `Array.prototype.reduce()` with the spread operator (`...`). The first (leftmost) function can accept one or more arguments, while the remaining functions must be unary.

```js
const pipeFunctions = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args)),
  );
```

Here is an example of how to use `pipeFunctions` to create a new function `multiplyAndAdd5` that multiplies two numbers and then adds 5 to the result:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
const multiplyAndAdd5 = pipeFunctions(multiply, add5);
multiplyAndAdd5(5, 2); // 15
```

In this example, `multiplyAndAdd5` is a new function that takes two arguments, `5` and `2`, and applies `multiply` to them first, resulting in `10`, and then applies `add5` to the result, resulting in `15`.
