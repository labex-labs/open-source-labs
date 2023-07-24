# Remove Keys from Object

To remove specific keys from an object, use the `omit` function which takes an object and an array of keys to remove.

- The `Object.keys()` method is used to get all the keys of the object
- The `Array.prototype.filter()` method is then used to remove the specified keys from the list of keys
- Finally, `Array.prototype.reduce()` is used to create a new object with the remaining key-value pairs

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

Example usage:

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
