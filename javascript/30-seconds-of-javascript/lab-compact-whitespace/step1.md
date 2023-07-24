# Function to Compact Whitespaces in a String

To compact whitespaces in a string, use the `compactWhitespace()` function.

- It uses `String.prototype.replace()` with a regular expression to replace all occurrences of 2 or more whitespace characters with a single space.
- The function takes a string as an argument and returns the compacted string.

```js
const compactWhitespace = (str) => str.replace(/\s{2,}/g, " ");
```

Example usage:

```js
compactWhitespace("Lorem    Ipsum"); // 'Lorem Ipsum'
compactWhitespace("Lorem \n Ipsum"); // 'Lorem Ipsum'
```
