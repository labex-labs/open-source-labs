# How to Group Array Elements

If you want to practice coding, you can start by opening the Terminal/SSH and typing `node`. Once you're ready, you can group the elements of an array based on a given function using the following steps:

1. Use `Array.prototype.map()` to map the values of the array to a function or property name.
2. Use `Array.prototype.reduce()` to create an object where the keys are produced from the mapped results.

Here's an example code snippet:

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

To test the code, you can use the following examples:

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

These will return objects with keys based on the specified function and values that are arrays of the original elements that match the function.
