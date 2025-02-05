# Array Difference

To find the difference between two arrays, follow these steps:

1. Open the Terminal/SSH and type `node` to start coding.

2. Create a `Set` from array `b` to extract the unique values from `b`.

3. Use `Array.prototype.filter()` on array `a` to keep only the values that are not in array `b`, using `Set.prototype.has()`.

Here is the code:

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

Example usage:

```js
difference([1, 2, 3, 3], [1, 2, 4]); // Output: [3, 3]
```
