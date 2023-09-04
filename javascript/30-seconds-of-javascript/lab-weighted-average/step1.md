# How to Calculate Weighted Average in JavaScript

To calculate the weighted average of two or more numbers in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.reduce()` to create the weighted sum of the values and the sum of the weights.
3. Divide the weighted sum of the values by the sum of the weights to get the weighted average.

Here's the JavaScript code for the `weightedAverage` function:

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0],
  );
  return sum / weightSum;
};
```

You can use the `weightedAverage` function to calculate the weighted average of an array of numbers and an array of weights like this:

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
