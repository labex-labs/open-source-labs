# How to Extend a 3-Digit Color Code to a 6-Digit Color Code

To practice coding, open the Terminal/SSH and type `node`. You can use the following function to extend a 3-digit color code to a 6-digit color code:

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

To convert a 3-digit RGB notated hexadecimal color-code to the 6-digit form, follow these steps:

- Use `Array.prototype.map()`, `String.prototype.split()`, and `Array.prototype.join()` to join the mapped array.
- Use `Array.prototype.slice()` to remove `#` from the string start since it's added once.

Here are some examples:

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
