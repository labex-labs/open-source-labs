# How to Check for Duplicates in an Array

To check if an array has duplicate values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Set` to get the unique values in the array.
3. Use `Set.prototype.size` and `Array.prototype.length` to check if the count of the unique values is the same as the number of elements in the original array.

Here's an example code snippet that checks for duplicates in an array:

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

You can test this function with the following code:

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

The `hasDuplicates` function returns `true` if there are any duplicate values in the array, and `false` otherwise.
