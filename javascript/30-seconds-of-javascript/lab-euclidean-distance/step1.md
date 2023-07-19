# Euclidean Distance Calculation

To calculate the distance between two points in any number of dimensions, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Object.keys()` and `Array.prototype.map()` to map each coordinate to its difference between the two points.
3. Use `Math.hypot()` to calculate the Euclidean distance between the two points.

Here's an example code snippet to help you get started:

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

You can try out the function using these sample inputs:

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
