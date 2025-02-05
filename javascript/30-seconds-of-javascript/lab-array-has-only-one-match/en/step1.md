# Function to Check if Array Has Only One Match

To check if an array has only one value matching the given function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` in combination with `fn` to find all matching array elements.
3. Use `Array.prototype.length` to check if only one element matches `fn`.

Here's the code:

```js
const hasOne = (arr, fn) => arr.filter(fn).length === 1;
```

And here's an example:

```js
hasOne([1, 2], (x) => x % 2); // true
hasOne([1, 3], (x) => x % 2); // false
```
