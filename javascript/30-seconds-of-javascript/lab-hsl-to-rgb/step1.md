# Convert HSL to RGB using JavaScript

To convert a color tuple in HSL format to RGB, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the [HSL to RGB conversion formula](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB) to convert the color tuple to the appropriate format.
3. Ensure that the input parameters are within the following ranges: H: [0, 360], S: [0, 100], L: [0, 100].
4. The output values should be within the range [0, 255].

Here is the JavaScript code for the HSL to RGB conversion formula:

```js
const HSLToRGB = (h, s, l) => {
  s /= 100;
  l /= 100;
  const k = (n) => (n + h / 30) % 12;
  const a = s * Math.min(l, 1 - l);
  const f = (n) =>
    l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
  return [255 * f(0), 255 * f(8), 255 * f(4)];
};
```

To use the function, provide the H, S, and L values as arguments:

```js
HSLToRGB(13, 100, 11); // [56.1, 12.155, 0]
```
