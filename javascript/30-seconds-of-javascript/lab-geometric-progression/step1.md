# Geometric Progression

To generate a geometric progression, use the `geometricProgression` function. This function takes three arguments: `end`, `start` (optional), and `step` (optional).

The `end` parameter specifies the end value of the progression. If you omit the `start` parameter, it defaults to `1`. If you omit the `step` parameter, it defaults to `2`.

The function initializes an array containing the numbers in the specified range where `start` and `end` are inclusive and the ratio between two terms is `step`. It returns an error if `step` equals `1`.

To create the array, the function uses `Array.from()`, `Math.log()`, and `Math.floor()`. It then fills the array with the desired values in a range using `Array.prototype.map()`.

Here's an example usage:

```js
geometricProgression(256); // [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometricProgression(256, 3); // [3, 6, 12, 24, 48, 96, 192]
geometricProgression(256, 1, 4); // [1, 4, 16, 64, 256]
```
