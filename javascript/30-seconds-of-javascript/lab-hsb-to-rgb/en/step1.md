# HSB to RGB Conversion

To convert a HSB color tuple to RGB format, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use the [HSB to RGB conversion formula](https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB) to convert to the appropriate format.
- The input parameters should be in the range of H: [0, 360], S: [0, 100], B: [0, 100].
- All output values should be in the range of [0, 255].

Here's the code that you can use to convert HSB to RGB:

```js
const HSBToRGB = (h, s, b) => {
  s /= 100;
  b /= 100;
  const k = (n) => (n + h / 60) % 6;
  const f = (n) => b * (1 - s * Math.max(0, Math.min(k(n), 4 - k(n), 1)));
  return [255 * f(5), 255 * f(3), 255 * f(1)];
};
```

For example, if you want to convert the HSB color tuple (18, 81, 99) to RGB format, you can use the following code:

```js
HSBToRGB(18, 81, 99); // [252.45, 109.31084999999996, 47.965499999999984]
```
