# RGB to HSB Conversion

To convert a RGB color tuple to HSB format, you can follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the [RGB to HSB conversion formula](https://en.wikipedia.org/wiki/HSL_and_HSV#From_RGB) to convert the RGB color tuple to the appropriate HSB format.
3. The input parameters range is [0, 255], while the resulting values have a range of:

- H: [0, 360]
- S: [0, 100]
- B: [0, 100]

Here is the function in JavaScript:

```js
const RGBToHSB = (r, g, b) => {
  r /= 255;
  g /= 255;
  b /= 255;
  const v = Math.max(r, g, b),
    n = v - Math.min(r, g, b);
  const h =
    n === 0
      ? 0
      : n && v === r
        ? (g - b) / n
        : v === g
          ? 2 + (b - r) / n
          : 4 + (r - g) / n;
  return [60 * (h < 0 ? h + 6 : h), v && (n / v) * 100, v * 100];
};
```

You can call the function like this:

```js
RGBToHSB(252, 111, 48);
// [18.529411764705856, 80.95238095238095, 98.82352941176471]
```
