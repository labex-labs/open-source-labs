# Function to Check if a String is Uppercase

To check if a string is in uppercase, follow these steps:

1. Open the Terminal/SSH.
2. Type `node`.
3. Use the function `isUpperCase()` to convert the given string to uppercase, using `String.prototype.toUpperCase()`, and compare it to the original string.
4. The function will return `true` if the string is in uppercase and `false` if it is not.

Here is an example code:

```js
const isUpperCase = (str) => str === str.toUpperCase();

console.log(isUpperCase("ABC")); // true
console.log(isUpperCase("A3@$")); // true
console.log(isUpperCase("aB4")); // false
```
