# Filter Unique Array Values Based on Function

Here's how to create an array that contains only the non-unique values by filtering out the unique ones based on a comparator function, `fn`:

```js
const filterUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.some((x, j) => (i !== j) === fn(v, x, i, j)));
```

To use this function, call `filterUniqueBy()` with two arguments: the array you want to filter and the comparator function. The comparator function should take four arguments: the values of the two elements being compared and their indexes.

For example, if you have an array of objects and you want to filter out the objects with unique `id` values, you can do this:

```js
filterUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 3, value: "d" },
    { id: 0, value: "e" },
  ],
  (a, b) => a.id == b.id,
); // [ { id: 0, value: 'a' }, { id: 0, value: 'e' } ]
```

To start practicing coding, open the Terminal/SSH and type `node`.
