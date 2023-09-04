# How to Filter Out Values from an Array Based on a Function

To filter out all values from an array based on a given comparator function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` and `Array.prototype.findIndex()` to find the appropriate values.
3. Omit the last argument, `comp`, to use a default strict equality comparator.
4. Use the following code:

```js
const differenceWith = (arr, val, comp = (a, b) => a === b) =>
  arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1);
```

5. Test your function with the following examples:

```js
differenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0],
  (a, b) => Math.round(a) === Math.round(b),
); // Expected output: [1, 1.2]

differenceWith([1, 1.2, 1.3], [1, 1.3, 1.5]); // Expected output: [1.2]
```
