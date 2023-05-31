# How to Get Last N Elements of an Array in JavaScript

To get the last `n` elements of an array in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use `Array.prototype.slice()` with a start value of `-n` to get the last `n` elements of the array.

Here's the JavaScript code to get the last `n` elements of an array:

```js
const lastN = (arr, n) => arr.slice(-n);
```

To test the code, call the `lastN()` function with the array and the number of elements you want to get, like this:

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
