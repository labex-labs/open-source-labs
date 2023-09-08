# Function to Map Object Values

To map the values of an object using a provided function to generate a new object with the same keys, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` to iterate over the keys of the object.
3. Use `Array.prototype.reduce()` to create a new object with the same keys and mapped values using the provided function `fn`.
4. The code below demonstrates the implementation of the `mapValues` function.

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

Here is an example usage of the `mapValues` function:

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
