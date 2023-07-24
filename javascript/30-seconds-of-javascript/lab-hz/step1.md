# Function Frequency Calculation

To measure the frequency of a function execution per second (hz/hertz), use the `hz` function. You can do this by following these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `performance.now()` to get the difference in milliseconds before and after the iteration loop to calculate the time elapsed executing the function `iterations` times.
3. Convert milliseconds to seconds and divide it by the time elapsed to return the number of cycles per second.
4. If you want to use the default of 100 iterations, omit the second argument, `iterations`.

```js
const hz = (fn, iterations = 100) => {
  const before = performance.now();
  for (let i = 0; i < iterations; i++) fn();
  return (1000 * iterations) / (performance.now() - before);
};
```

Here's an example of using the `hz` function to compare the performance of two functions that calculate the sum of an array of 10,000 numbers:

```js
const numbers = Array(10000)
  .fill()
  .map((_, i) => i);

const sumReduce = () => numbers.reduce((acc, n) => acc + n, 0);
const sumForLoop = () => {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) sum += numbers[i];
  return sum;
};

Math.round(hz(sumReduce)); // 572
Math.round(hz(sumForLoop)); // 4784
```

In this example, `sumReduce` is faster than `sumForLoop` because it has a lower frequency of function execution.
