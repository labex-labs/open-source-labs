# Function to Return N Minimum Elements of an Array

To practice coding, open the Terminal/SSH and type `node`. Use the `minN` function to return the `n` minimum elements from an array.

Here's how to use the function:

- Use `Array.prototype.sort()` and the spread operator (`...`) to create a shallow clone of the array and sort it in ascending order.
- Use `Array.prototype.slice()` to get the specified number of elements.
- If you omit the second argument, `n`, the function will return a one-element array.
- If `n` is greater than or equal to the length of the provided array, the function will return the original array, sorted in ascending order.

```js
const minN = (arr, n = 1) => [...arr].sort((a, b) => a - b).slice(0, n);
```

Here are some examples:

```js
minN([1, 2, 3]); // [1]
minN([1, 2, 3], 2); // [1, 2]
```
