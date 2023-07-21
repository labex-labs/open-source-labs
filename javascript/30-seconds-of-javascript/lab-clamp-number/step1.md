# Function to Clamp a Number within a Range

To clamp a number within a specified range, use the `clampNumber` function.

To start, open the Terminal/SSH and type `node` to practice coding.

The `clampNumber` function takes in three parameters: `num`, `a`, and `b`. It clamps `num` within the inclusive range specified by the boundary values `a` and `b` and returns the result.

If `num` falls within the range, the function returns `num`. Otherwise, it returns the nearest number in the range.

Here's the code for the `clampNumber` function:

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

And here are some examples of how to use the function:

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
