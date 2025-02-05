# Initializing a Mapped Array in JavaScript

To initialize a mapped array in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array()` constructor to create an array of the desired length.
3. Use `Array.prototype.fill()` to fill the array with `null` values.
4. Use `Array.prototype.map()` to fill the array with the desired values, using the provided function, `mapFn`.
5. Omit the second argument, `mapFn`, to map each element to its index.

Here's an example code snippet:

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

You can use the `initializeMappedArray` function to create a mapped array with the desired values:

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
