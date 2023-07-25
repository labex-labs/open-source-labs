# Function to Remove Whitespaces

To remove whitespaces from a string, use the following function.

- Use `String.prototype.replace()` with a regular expression to replace all occurrences of whitespace characters with an empty string.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

For example,

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'
```

To start practicing coding, open the Terminal/SSH and type `node`.
