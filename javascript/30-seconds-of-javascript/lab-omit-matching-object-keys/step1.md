# Removing Object Keys Based on Callback Function

To remove object keys based on a callback function, use `omitBy` function.

- `omitBy` creates an object consisting of properties that return falsy for the given function.
- `Object.keys()` and `Array.prototype.filter()` are used to remove keys for which `fn` returns a truthy value.
- `Array.prototype.reduce()` converts the filtered keys back to an object with the corresponding key-value pairs.
- The callback function takes two arguments: `value` and `key`.
- The example below shows how `omitBy` is used to remove numeric keys from an object.

```js
const omitBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => !fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});

omitBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number"); // { b: '2' }
```
