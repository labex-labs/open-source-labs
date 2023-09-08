# Transpose a Matrix in JavaScript

To transpose a two-dimensional array in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` to create the transpose of the given two-dimensional array. The `map()` method creates a new array with the results of calling a provided function on every element in the array.
3. The provided function should take two arguments: the current element of the array and its index. In this case, we only need the index to create the transpose.
4. Use the index to access the corresponding elements in each row of the two-dimensional array and create a new array with those elements. This will be the new row in the transposed array.
5. Repeat the previous step for each column in the two-dimensional array to create the complete transposed array.

Here's the code to transpose a two-dimensional array in JavaScript:

```js
const transpose = (arr) => arr[0].map((col, i) => arr.map((row) => row[i]));

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]);
// [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```
