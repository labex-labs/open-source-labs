# Array Unique Symmetric Difference Function

To practice coding, open the Terminal/SSH and type `node`. The following function returns the unique symmetric difference between two arrays. It removes duplicate values from either array.

To achieve this, use `Array.prototype.filter()` and `Array.prototype.includes()` on each array to remove values contained in the other. Create a `Set` from the results to remove duplicate values.

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v)),
  ]),
];
```

Use the function as shown below:

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
