# A Function to Find Array Symmetric Difference

To find symmetric difference between two arrays using a provided function as a comparator, follow these steps:

1. Open Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` and `Array.prototype.findIndex()` methods to find the appropriate values.
3. Use the given code to perform the operation.

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1),
];
```

For example, consider the following input:

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b),
); // [1, 1.2, 3.9]
```

The above code will return `[1, 1.2, 3.9]` as the symmetric difference between the two arrays.
