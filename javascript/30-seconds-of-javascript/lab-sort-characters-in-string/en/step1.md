# Here's how to sort characters in a string:

Use the following code to sort the characters in a string alphabetically:

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

To start, open the Terminal/SSH and type `node` to begin practicing coding.

Example usage:

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
