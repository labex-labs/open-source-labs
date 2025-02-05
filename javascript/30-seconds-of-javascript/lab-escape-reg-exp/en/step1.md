# How to Escape Regular Expressions in JavaScript

To escape a string to use in a regular expression in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.replace()` to escape special characters.
3. Copy and paste the following code snippet:

```js
const escapeRegExp = (str) => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
```

4. Use `escapeRegExp()` function to escape special characters in a string.

Here's an example:

```js
escapeRegExp("(test)"); // \\(test\\)
```

With these steps, you can now easily escape any special character in a regular expression in JavaScript.
