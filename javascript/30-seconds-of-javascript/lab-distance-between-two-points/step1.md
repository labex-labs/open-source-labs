# Calculating the Distance Between Two Points

To calculate the distance between two points, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Math.hypot()` to calculate the Euclidean distance between two points.
3. Implement the code below, replacing the `x0`, `y0`, `x1`, and `y1` values with the coordinates of your points.

```js
const distance = (x0, y0, x1, y1) => Math.hypot(x1 - x0, y1 - y0);
```

Here's an example of how to use this function:

```js
distance(1, 1, 2, 3); // ~2.2361
```

This will output the distance between the points `(1, 1)` and `(2, 3)`.
