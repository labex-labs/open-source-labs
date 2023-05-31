# Function to Check if Array Has Multiple Matches

To check if an array has more than one value matching a given function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.filter()` in combination with `fn` to find all matching array elements.
3. Use `Array.prototype.length` to check if more than one element matches `fn`.

Here's the code you can use:

```js
const hasMany = (arr, fn) => arr.filter(fn).length > 1;
```

And here are some examples:

```js
hasMany([1, 3], (x) => x % 2); // true
hasMany([1, 2], (x) => x % 2); // false
```
