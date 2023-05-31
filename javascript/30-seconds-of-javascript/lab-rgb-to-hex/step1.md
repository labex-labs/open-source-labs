# RGB to Hex Converter

To convert RGB values to a hexadecimal color code:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the following function:

```js
const RGBToHex = (r, g, b) =>
  ((r << 16) + (g << 8) + b).toString(16).padStart(6, "0");
```

3. Call the function with the RGB values as arguments to get a 6-digit hexadecimal value.

For example:

```js
RGBToHex(255, 165, 1); // 'ffa501'
```
