# Mapped Array Symmetric Difference

To get started with coding, open the Terminal/SSH and type `node`.

This function returns the symmetric difference between two arrays, after applying the provided function to each element of both arrays. Here's how it works:

- Create a `Set` from each array to get the unique values of each one after applying `fn` to them.
- Use `Array.prototype.filter()` on each of them to only keep values not contained in the other.

Here's the code for the `symmetricDifferenceBy` function:

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

You can use `symmetricDifferenceBy` like this:

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
