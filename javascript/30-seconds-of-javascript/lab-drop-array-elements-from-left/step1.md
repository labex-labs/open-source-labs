# Removing Array Elements From the Left

To start practicing coding, open the Terminal/SSH and type `node`.

Here's a function that creates a new array with a specified number of elements removed from the left:

```js
const drop = (arr, n = 1) => arr.slice(n);
```

The function uses `Array.prototype.slice()` to remove the specified number of elements from the left. If you omit the last argument, `n`, the function will use a default value of `1`.

Here are some examples of using the `drop` function:

```js
drop([1, 2, 3]); // [2, 3]
drop([1, 2, 3], 2); // [3]
drop([1, 2, 3], 42); // []
```
