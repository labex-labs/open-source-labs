# How to Insert a Value at a Specific Index in an Array using JavaScript

To insert a value at a specific index in an array using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.splice()` method with an appropriate index and a delete count of `0`, spreading the given values to be inserted.
3. The `insertAt` function takes an array, an index, and one or more values to be inserted after the specified index.
4. The function mutates the original array and returns the modified array.

Here's an example of the `insertAt` function in action:

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

In the example above, the `insertAt` function is used to insert the value `5` after the second index of the `myArray` array, and to insert the values `4`, `6`, and `8` after the first index of the `otherArray` array.
