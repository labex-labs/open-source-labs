# Reversing a Number

To reverse a number using JavaScript, you can use the `reverseNumber()` function with the following steps:

1. Convert the number `n` to a string using `Object.prototype.toString()`.
2. Use `String.prototype.split()`, `Array.prototype.reverse()` and `Array.prototype.join()` to get the reversed value of `n` as a string.
3. Convert the string back to a number using `parseFloat()`.
4. Preserve the sign of the number using `Math.sign()`.

Here's the code for the `reverseNumber()` function:

```js
const reverseNumber = (n) =>
  parseFloat(`${n}`.split("").reverse().join("")) * Math.sign(n);
```

You can test the function with these examples:

```js
reverseNumber(981); // 189
reverseNumber(-500); // -5
reverseNumber(73.6); // 6.37
reverseNumber(-5.23); // -32.5
```
