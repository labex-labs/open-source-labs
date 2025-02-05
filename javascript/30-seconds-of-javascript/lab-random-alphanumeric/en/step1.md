# How to Generate a Random Alphanumeric String in JavaScript

To generate a random string of alphanumeric characters in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a new array with the specified length using `Array.from()`.
3. Generate a random floating-point number using `Math.random()`.
4. Convert the number to an alphanumeric string using `Number.prototype.toString()` with a `radix` value of `36`.
5. Remove the integral part and decimal point from each generated number using `String.prototype.slice()`.
6. Repeat this process as many times as required, up to `length`, using `Array.prototype.some()`, as it produces a variable-length string each time.
7. Trim down the generated string if it's longer than the given `length` using `String.prototype.slice()`.
8. Return the generated string.

Here's the code:

```js
const randomAlphaNumeric = (length) => {
  let s = "";
  Array.from({ length }).some(() => {
    s += Math.random().toString(36).slice(2);
    return s.length >= length;
  });
  return s.slice(0, length);
};
```

You can call the `randomAlphaNumeric()` function with the desired length as the argument. For example:

```js
randomAlphaNumeric(5); // '0afad'
```
