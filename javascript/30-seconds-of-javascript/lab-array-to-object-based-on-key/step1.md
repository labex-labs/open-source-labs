# Converting an Array to an Object Based on a Specific Key

To convert an array into an object based on a specific key and exclude that key from each value, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `Array.prototype.reduce()` to create an object from the provided array.
- Use object destructuring to extract the value of the given `key` and the associated `data`, and then add the key-value pair to the object.

Here's an example implementation:

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

You can then use the function like this:

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" },
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
