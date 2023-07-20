# Converting Degrees to Radians

To convert an angle from degrees to radians, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start coding.
3. Use the degree to radian formula along with `Math.PI`.
4. Apply the formula to the angle in degrees to get the angle in radians.

Here's the formula in JavaScript:

```js
const degreesToRads = (deg) => (deg * Math.PI) / 180.0;
```

For example, if you want to convert 90 degrees to radians, you can use the `degreesToRads` function like this:

```js
degreesToRads(90.0); // ~1.5708
```
