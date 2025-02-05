# How to Filter Non-Unique Values in an Array in JavaScript

To filter non-unique values in an array in JavaScript, you can create a new array with only the unique values. Here's how:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Set` constructor and the spread operator (`...`) to create an array of the unique values in the original array.
3. Use `Array.prototype.filter()` to create an array containing only the unique values.

Here's an example function that does this:

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

You can use this function with any array to filter out the non-unique values. For example:

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
