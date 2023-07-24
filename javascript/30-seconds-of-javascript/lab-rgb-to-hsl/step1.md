# RGB to HSL Conversion

To convert an RGB color tuple to HSL format, follow these steps:

1. Open the Terminal/SSH to start practicing coding.
2. Type `node` and press enter.
3. Use the [RGB to HSL conversion formula](https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/) to convert to the appropriate format.
4. Ensure that all input parameters fall within the range of [0, 255].
5. The resulting values should fall within the range of H: [0, 360], S: [0, 100], L: [0, 100].

Here is an example of the RGBToHSL function in JavaScript:

```js
const RGBToHSL = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const l = Math.max(r, g, b);
  const s = l - Math.min(r, g, b);
  const h = s
    ? l === r
      ? (g - b) / s
      : l === g
      ? 2 + (b - r) / s
      : 4 + (r - g) / s
    : 0;
  return [
    60 * h < 0 ? 60 * h + 360 : 60 * h,
    100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0),
    (100 * (2 * l - s)) / 2,
  ];
};
```

Here is an example of how to use the RGBToHSL function:

```js
RGBToHSL(45, 23, 11); // [21.17647, 60.71428, 10.98039]
```
