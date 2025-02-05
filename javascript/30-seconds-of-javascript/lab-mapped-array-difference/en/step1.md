# Function to Return the Difference of Two Arrays by Mapping

To get started with coding, open your Terminal/SSH and type `node`.

This function takes two arrays and applies the provided function to each element in both arrays to return their difference.

To do this:

- Create a `Set` by applying the function (`fn`) to each element in the second array (`b`).
- Use `Array.prototype.map()` to apply the function (`fn`) to each element in the first array (`a`).
- Use `Array.prototype.filter()` in combination with the function (`fn`) on the first array (`a`) to only keep values not contained in the second array (`b`), using `Set.prototype.has()`.

Here's the code for the function:

```js
const differenceBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return a.map(fn).filter((el) => !s.has(el));
};
```

Here are some examples of how to use the function:

```js
differenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [1]
differenceBy([{ x: 2 }, { x: 1 }], [{ x: 1 }], (v) => v.x); // [2]
```
