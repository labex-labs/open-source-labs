# Filtering Non-Unique Array Values with a Function

To start practicing coding, open the Terminal/SSH and type `node`.

This code filters out non-unique values from an array, based on a provided comparator function. Here are the steps to achieve this:

1. Use `Array.prototype.filter()` and `Array.prototype.every()` to create a new array with only the unique values based on the comparator function `fn`.
2. The comparator function takes four arguments: the values of the two elements being compared and their indexes.
3. The function `filterNonUniqueBy` implements the above steps and returns the unique values array.

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

Here is an example of how to use this function:

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" },
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

This code is concise, clear and coherent and should work as expected.
