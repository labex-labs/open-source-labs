# How to Check if Two Arrays Have a Common Item

To check if two arrays have a common item, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a `Set` from `b` to get the unique values in `b`.
3. Use `Array.prototype.some()` on `a` to check if any of its values are contained in `b`, using `Set.prototype.has()`.
4. Use the `intersects` function provided below to test the arrays.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

Use the `intersects` function to check if two arrays intersect:

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

By following these steps and using the provided code, you can easily check if two arrays have a common item.
