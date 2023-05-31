# Function to pick object keys that match a given condition

To pick object keys that match a given condition, use the `pickBy()` function. This function creates a new object composed of the properties for which the given function returns a truthy value.

- Use `Object.keys()` and `Array.prototype.filter()` to remove the keys for which `fn` returns a falsy value.
- Use `Array.prototype.reduce()` to convert the filtered keys back to an object with the corresponding key-value pairs.
- The callback function is invoked with two arguments: (value, key).

Here's the code for the `pickBy()` function:

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

You can use this function to pick keys that match a condition. For example:

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
