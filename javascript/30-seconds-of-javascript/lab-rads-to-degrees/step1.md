# Converting Radians to Degrees

To convert an angle from radians to degrees, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the following formula: `degrees = radians * (180 / Math.PI)`
3. Replace `radians` in the formula with the value you want to convert.
4. The result will be in degrees.

Here's an example:

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

This will convert `π/2` radians to `90` degrees.
