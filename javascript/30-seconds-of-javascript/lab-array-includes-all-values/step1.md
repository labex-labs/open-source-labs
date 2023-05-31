# Function to Check if an Array Includes All Values

If you want to check whether all the elements in an array `values` are included in another array `arr`, you can use the `includesAll` function in JavaScript.

To start using the function, open the Terminal/SSH and type `node`.

Here's how the `includesAll` function works:

- It uses `Array.prototype.every()` and `Array.prototype.includes()` methods to check if all elements in `values` are included in `arr`.
- If all elements in `values` are included in `arr`, the function will return `true`. Otherwise, it will return `false`.

```js
const includesAll = (arr, values) => values.every((v) => arr.includes(v));
```

Here's an example of how to use the `includesAll` function:

```js
includesAll([1, 2, 3, 4], [1, 4]); // true
includesAll([1, 2, 3, 4], [1, 5]); // false
```
