# Converting RGB String to an Array

To convert an `rgb()` color string to an array of values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.match()` to get an array of 3 strings with the numeric values.
3. Use `Array.prototype.map()` in combination with `Number` to convert them into an array of numeric values.

Here's the code that you can use:

```js
const toRGBArray = (rgbStr) => rgbStr.match(/\d+/g).map(Number);
```

To test the function, call it with an `rgb()` color string as the argument, like this:

```js
toRGBArray("rgb(255, 12, 0)"); // [255, 12, 0]
```
