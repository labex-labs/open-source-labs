# How to Find Unique Values in Array with JavaScript

To find all unique values in an array, you can follow these steps in JavaScript:

1. Create a `Set` from the given array to discard duplicated values.
2. Use the spread operator (`...`) to convert the `Set` back to an array.

Here's an example code snippet:

```js
const getUniqueValues = (arr) => [...new Set(arr)];
```

You can call the function and pass an array to it, like this:

```js
getUniqueValues([1, 2, 2, 3, 4, 4, 5]); // [1, 2, 3, 4, 5]
```

This will return an array with all the unique values from the original array, without any duplicates.
