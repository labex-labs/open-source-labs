# How to Compose Functions in JavaScript

To start practicing coding using function composition in JavaScript, open the Terminal/SSH and type `node`.

Here's an example of how to perform right-to-left function composition in JavaScript:

1. Use `Array.prototype.reduce()` to perform right-to-left function composition.
2. The last (rightmost) function can accept one or more arguments; the remaining functions must be unary.
3. Define the `compose` function that will take any number of functions as arguments and return a new function that composes them.
4. Call the `compose` function with the desired functions in the desired order.
5. Call the new composed function with any necessary arguments.

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

For example, let's say we have two functions:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

We can compose these functions using `compose`:

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

Now we can call `multiplyAndAdd5` with the desired arguments:

```js
multiplyAndAdd5(5, 2); // 15
```
