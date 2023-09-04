# Function to Index an Array

To index an array using a function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()` to create an object from the array.
3. Apply the provided function to each value of the array to produce a key and add the key-value pair to the object.

Here's an example code snippet:

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

You can use this function as follows:

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" },
  ],
  (x) => x.id,
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

This function creates an object from an array by mapping each value to a key using a provided function. The resulting object contains key-value pairs where the keys are produced by the function and the values are the original array elements.
