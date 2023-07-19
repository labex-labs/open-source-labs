# Cartesian Product

To calculate the cartesian product of two arrays, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()`, `Array.prototype.map()`, and the spread operator (`...`) to generate all possible element pairs from the two arrays.
3. Use the following code:

```js
const cartesianProduct = (a, b) =>
  a.reduce((p, x) => [...p, ...b.map((y) => [x, y])], []);
```

Example:

```js
cartesianProduct(["x", "y"], [1, 2]);
// [['x', 1], ['x', 2], ['y', 1], ['y', 2]]
```

This will generate all possible combinations of elements from the two arrays.
