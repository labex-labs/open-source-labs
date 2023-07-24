# Drop Array Elements From the Right

To remove a specified number of elements from the right of an array, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.slice()` to remove the specified number of elements from the right.
3. If you want to remove only one element, you can omit the last argument, `n`, and the default value of `1` will be used.

Here's an example code snippet:

```js
const dropRight = (arr, n = 1) => arr.slice(0, -n);
```

You can test this function with the following examples:

```js
dropRight([1, 2, 3]); // [1, 2]
dropRight([1, 2, 3], 2); // [1]
dropRight([1, 2, 3], 42); // []
```
