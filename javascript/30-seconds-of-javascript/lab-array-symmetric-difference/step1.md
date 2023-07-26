# Array Symmetric Difference

To find the symmetric difference between two arrays and include duplicate values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a `Set` from each array to get the unique values of each one.
3. Use `Array.prototype.filter()` on each of them to only keep values not contained in the other.

Here's the code:

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

You can use the following examples to test the function:

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
