# How to Swapcase a String in JavaScript

To swap the case of a string in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the spread operator (`...`) to convert the input string `str` into an array of characters.
3. Use `String.prototype.toLowerCase()` and `String.prototype.toUpperCase()` to convert lowercase characters to uppercase and vice versa.
4. Use `Array.prototype.map()` to apply the transformation to each character, and `Array.prototype.join()` to combine the characters back into a string.
5. Note that swapping the case of a string twice might not necessarily result in the original string.

Here's an example code snippet that demonstrates how to swap the case of a string in JavaScript:

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Output: 'hELLO WORLD!'
```
