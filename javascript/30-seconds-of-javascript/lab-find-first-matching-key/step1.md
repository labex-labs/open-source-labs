# Function to Find First Key Matching a Test

To find the first key in an object that matches a given test function, use the `findKey()` function. First, obtain all the object properties using `Object.keys()`. Then, apply the test function to each key-value pair using `Array.prototype.find()`. The test function should take in three arguments: the value, the key, and the object. The function returns the first key that satisfies the test function or `undefined` if none is found.

Here's an example implementation of `findKey()`:

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

To use `findKey()`, pass in the object and the test function as arguments:

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true },
  },
  (x) => x["active"]
); // 'barney'
```

In this example, `findKey()` returns the first key in the object where the value of the `active` property is `true`, which is `'barney'`.
