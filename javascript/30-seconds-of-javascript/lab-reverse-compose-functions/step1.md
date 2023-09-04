# Reversing Function Composition

To start practicing coding, open the Terminal/SSH and type `node`.

Here's how to perform left-to-right function composition:

- Use `Array.prototype.reduce()` method to perform left-to-right function composition.
- The first (leftmost) function can accept one or more arguments, while the remaining functions must be unary.

```js
const composeRight = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        g(f(...args)),
  );
```

For example:

```js
const add = (x, y) => x + y;
const square = (x) => x * x;
const addAndSquare = composeRight(add, square);
addAndSquare(1, 2); // 9
```
