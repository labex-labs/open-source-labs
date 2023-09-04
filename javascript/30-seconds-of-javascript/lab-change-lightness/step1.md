# How to Change the Lightness of an HSL Color

To change the lightness value of an `hsl()` color string, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use `String.prototype.match()` to get an array of three strings with the numeric values from the `hsl()` string.

3. Use `Array.prototype.map()` in combination with `Number` to convert the strings into an array of numeric values.

4. Ensure the lightness value falls within the valid range (between `0` and `100`) using `Math.max()` and `Math.min()`.

5. Use a template literal to create a new `hsl()` string with the updated lightness value.

Here's an example code snippet that implements these steps:

```js
const changeLightness = (delta, hslStr) => {
  const [hue, saturation, lightness] = hslStr.match(/\d+/g).map(Number);

  const newLightness = Math.max(
    0,
    Math.min(100, lightness + parseFloat(delta)),
  );

  return `hsl(${hue}, ${saturation}%, ${newLightness}%)`;
};
```

You can then call the `changeLightness()` function with a delta value and an `hsl()` string to get a new `hsl()` string with the updated lightness value. For example:

```js
changeLightness(10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 60%)'
changeLightness(-10, "hsl(330, 50%, 50%)"); // 'hsl(330, 50%, 40%)'
```
