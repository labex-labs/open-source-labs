# Convert HSL to Array

To convert an `hsl()` color string to an array of values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.match()` to get an array of 3 strings with the numeric values.
3. Use `Array.prototype.map()` in combination with `Number` to convert them into an array of numeric values.

Here's the code to convert an `hsl()` color string to an array of numeric values:

```js
const toHSLArray = (hslStr) => hslStr.match(/\d+/g).map(Number);
```

Example usage:

```js
toHSLArray("hsl(50, 10%, 10%)"); // [50, 10, 10]
```
