# Function to Get Size of Array, Object, or String

To use this function, open the Terminal/SSH and type `node`. This function gets the size of an array, object or string.

To use it:

- Determine the type of `val` (`array`, `object` or `string`).
- Use the `Array.prototype.length` property for arrays.
- Use the `length` or `size` value if available, or the number of keys for objects.
- For strings, use the `size` of a [`Blob` object](https://developer.mozilla.org/en-US/docs/Web/API/Blob) created from `val`.

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
    ? val.size || val.length || Object.keys(val).length
    : typeof val === "string"
    ? new Blob([val]).size
    : 0;
```

Examples:

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
