# HSL to Object Conversion

To convert an `hsl()` color string into an object with the numeric values of each color, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `String.prototype.match()` to get an array of 3 strings with the numeric values.
- Convert the strings into an array of numeric values using `Array.prototype.map()` in combination with `Number`.
- Store the values into named variables using array destructuring.
- Create an appropriate object from the named variables.

```js
const toHSLObject = (hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);
  return { hue, saturation, lightness };
};
```

Example usage:

```js
toHSLObject("hsl(50, 10%, 10%)"); // { hue: 50, saturation: 10, lightness: 10 }
```
