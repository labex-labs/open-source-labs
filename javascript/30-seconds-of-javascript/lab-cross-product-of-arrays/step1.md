# Creating an Array Cross Product in JavaScript

To create an array cross product in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()`, `Array.prototype.map()`, and `Array.prototype.concat()` to produce every possible pair from the elements of the two arrays.
3. The function `xProd()` takes in two arrays as arguments and creates a new array out of the two supplied by creating each possible pair from the arrays.
4. Here's an example of the `xProd()` function in action:

```js
const xProd = (a, b) =>
  a.reduce((acc, x) => acc.concat(b.map((y) => [x, y])), []);

xProd([1, 2], ["a", "b"]); // [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
```

This will return an array containing all possible pairs of elements from the two input arrays.
