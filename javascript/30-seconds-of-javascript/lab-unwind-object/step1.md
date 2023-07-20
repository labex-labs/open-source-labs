# Unwind Object Function

To unwind an object by its array-valued property, use the `unwind` function.

- To get started with coding, open the Terminal/SSH and type `node`.
- The function uses object destructuring to exclude the key-value pair for the specified `key` from the object.
- Then, it uses `Array.prototype.map()` for the values of the given `key` to create an array of objects.
- Each object contains the original object's values, except for `key` which is mapped to its individual values.

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

Example usage:

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
