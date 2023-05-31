# Hamming Distance Calculation

To calculate the Hamming distance between two values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the XOR operator (`^`) to find the bit difference between the two numbers.
3. Convert the result to a binary string using `Number.prototype.toString()`.
4. Count the number of `1`s in the string using `String.prototype.match()`.
5. Return the count.

Here's the code for the `hammingDistance` function:

```js
const hammingDistance = (num1, num2) =>
  ((num1 ^ num2).toString(2).match(/1/g) || "").length;
```

You can test the function by running `hammingDistance(2, 3); // 1`.
