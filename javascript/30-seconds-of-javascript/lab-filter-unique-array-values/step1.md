# How to Filter Unique Values in an Array using JavaScript

To filter unique values in an array using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Set` constructor and the spread operator (`...`) to create an array of the unique values in your original array.
3. Use `Array.prototype.filter()` to create an array containing only the non-unique values.
4. Define a function called `filterUnique` that takes in an array as an argument and applies the above steps to it.
5. Call the `filterUnique` function with your array as the argument.

Here is an example code snippet to achieve this:

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

In the above code snippet, the `filterUnique` function takes in an array and applies the `Set` constructor and `Array.prototype.filter()` method to it to return an array with only the non-unique values.
