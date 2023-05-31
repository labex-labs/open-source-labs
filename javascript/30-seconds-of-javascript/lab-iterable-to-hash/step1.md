# Converting an Iterable to a Hash

To convert an iterable (object or array) into a hash (keyed data store), follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.values()` to get the values of the iterable.
3. Use `Array.prototype.reduce()` to iterate over the values and create an object that is keyed by the reference value.
4. Call the `toHash` function with the iterable and an optional key parameter to specify the reference value.

Here's an example implementation of the `toHash` function in JavaScript:

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

You can call the `toHash` function with different iterables and keys to create different hashes. For example:

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
