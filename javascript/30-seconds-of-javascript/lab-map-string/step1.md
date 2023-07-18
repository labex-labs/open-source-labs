# Function to Map Characters in a String

To use this function to map characters in a string, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `String.prototype.split()` and `Array.prototype.map()` to call the provided function, `fn`, for each character in the given string.
- Use `Array.prototype.join()` to recombine the array of characters into a new string.
- The callback function, `fn`, takes three arguments: the current character, the index of the current character, and the string `mapString` was called upon.

Here's the function code:

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

Example usage:

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
