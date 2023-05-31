# Check if Two Arrays Intersect

> To start practicing coding, open the Terminal/SSH and type `node`.

Determines if two arrays have a common item.

- Create a `Set` from `b` to get the unique values in `b`.
- Use `Array.prototype.some()` on `a` to check if any of its values are contained in `b`, using `Set.prototype.has()`.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some(x => s.has(x));
};
```

```js
intersects(['a', 'b'], ['b', 'c']); // true
intersects(['a', 'b'], ['c', 'd']); // false
```
