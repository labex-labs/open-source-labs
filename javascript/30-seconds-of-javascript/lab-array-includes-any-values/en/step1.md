# Checking if an Array Includes Any Values

To start practicing coding, open the Terminal/SSH and type `node`.

To check if an array includes at least one element from another array, use `Array.prototype.some()` and `Array.prototype.includes()`. Here is an example function:

```js
const includesAny = (arr, values) => values.some((v) => arr.includes(v));
```

You can call this function and pass in the two arrays you want to compare as arguments. The function will return a boolean value indicating whether at least one element of `values` is included in `arr`. Here are some examples:

```js
includesAny([1, 2, 3, 4], [2, 9]); // true
includesAny([1, 2, 3, 4], [8, 9]); // false
```
