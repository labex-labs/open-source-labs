# Function to Map Object Keys

To map the keys of an object using a provided function and generate a new object, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` to iterate over the object's keys.
3. Use `Array.prototype.reduce()` to create a new object with the same values and mapped keys using the provided function (`fn`).

Here's an example implementation of the `mapKeys` function:

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

You can test the function with an example input like this:

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
