# Checking for Approximate Number Equality in JavaScript

To practice coding, open the Terminal/SSH and type `node`. This code checks if two numbers are approximately equal to each other. To do this:

- Use the `Math.abs()` method to compare the absolute difference of the two values to `epsilon`.
- If you don't provide a third argument, `epsilon`, the function will use a default value of `0.001`.

Here's the code:

```js
const approximatelyEqual = (v1, v2, epsilon = 0.001) =>
  Math.abs(v1 - v2) < epsilon;
```

To test the function, you can call it with two numbers as arguments, like this:

```js
approximatelyEqual(Math.PI / 2.0, 1.5708); // true
```

This will return `true` because `Math.PI / 2.0` is approximately equal to `1.5708` with an epsilon of `0.001`.
