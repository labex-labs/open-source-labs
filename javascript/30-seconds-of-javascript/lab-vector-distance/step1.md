# Vector Distance Calculation

To calculate the distance between two vectors, follow these steps:

1. Open the Terminal/SSH to start practicing coding.
2. Type `node` to begin.
3. Use `Array.prototype.reduce()`, `Math.pow()`, and `Math.sqrt()` to find the Euclidean distance between the vectors.
4. Apply the `vectorDistance` formula, shown below:

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. Test the formula by entering two vectors in the following format: `vectorDistance([10, 0, 5], [20, 0, 10]);`
6. The output will be the distance between the two vectors: `11.180339887498949`.
