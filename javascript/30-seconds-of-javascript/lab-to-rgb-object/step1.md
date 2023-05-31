# Converting RGB to Object

To convert an `rgb()` color string to an object with the values of each color, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.match()` to get an array of 3 strings with the numeric values.
3. Use `Array.prototype.map()` in combination with `Number` to convert them into an array of numeric values.
4. Use array destructuring to store the values into named variables and create an appropriate object from them.

Here's the code you can use:

```js
const toRGBObject = (rgbStr) => {
  const [red, green, blue] = rgbStr.match(/\d+/g).map(Number);
  return { red, green, blue };
};

toRGBObject("rgb(255, 12, 0)"); // {red: 255, green: 12, blue: 0}
```
