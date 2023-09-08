# How to Find the Union of Two Arrays Based on a Function

To find the union of two arrays based on a function using Node.js, follow these steps:

1. Open the Terminal/SSH and type `node`.
2. Use the following code to create a `Set` with all values of `a` and values in `b` for which the comparator finds no matches in `a`, using `Array.prototype.findIndex()`:

```js
const unionWith = (a, b, comp) =>
  Array.from(
    new Set([...a, ...b.filter((x) => a.findIndex((y) => comp(x, y)) === -1)])
  );
```

3. Call the `unionWith` function with three arguments: the first array, the second array, and the comparator function.
4. The function returns every element that exists in any of the two arrays at least once, using the provided comparator function.
5. Here's an example of calling the `unionWith` function:

```js
unionWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
);
// [1, 1.2, 1.5, 3, 0, 3.9]
```

This will return `[1, 1.2, 1.5, 3, 0, 3.9]` as the union of the two arrays.
