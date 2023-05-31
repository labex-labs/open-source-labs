# Chunk Iterable

To chunk an iterable into smaller arrays of a specified size, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use a `for...of` loop over the given iterable, using `Array.prototype.push()` to add each new value to the current `chunk`.
3. Check if the current `chunk` is of the desired `size` using `Array.prototype.length` and `yield` the value if it is.
4. Check the final `chunk` using `Array.prototype.length` and `yield` it if it's non-empty.
5. Use the following code:

```js
const chunkify = function* (itr, size) {
  let chunk = [];
  for (const v of itr) {
    chunk.push(v);
    if (chunk.length === size) {
      yield chunk;
      chunk = [];
    }
  }
  if (chunk.length) yield chunk;
};
```

6. Use this code to test the function:

```js
const x = new Set([1, 2, 1, 3, 4, 1, 2, 5]);
[...chunkify(x, 2)]; // [[1, 2], [3, 4], [5]]
```
