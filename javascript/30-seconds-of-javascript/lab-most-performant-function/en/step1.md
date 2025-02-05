# How to Find the Most Performant Function in JavaScript

To find the most performant function in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.map()` to generate an array where each value is the total time taken to execute the function after `iterations` times.
3. Use the difference in `performance.now()` values before and after to get the total time in milliseconds to a high degree of accuracy.
4. Use `Math.min()` to find the minimum execution time, and return the index of that shortest time which corresponds to the index of the most performant function.
5. If you omit the second argument, `iterations`, the function will use a default of `10000` iterations.
6. Keep in mind that the more iterations you use, the more reliable the result but the longer it will take.

Here's an example code snippet:

```js
const mostPerformant = (fns, iterations = 10000) => {
  const times = fns.map((fn) => {
    const before = performance.now();
    for (let i = 0; i < iterations; i++) fn();
    return performance.now() - before;
  });
  return times.indexOf(Math.min(...times));
};
```

To use this function, pass an array of functions as the first argument and the number of iterations as the second argument (optional). For example:

```js
mostPerformant([
  () => {
    // Loops through the entire array before returning `false`
    [1, 2, 3, 4, 5, 6, 7, 8, 9, "10"].every((el) => typeof el === "number");
  },
  () => {
    // Only needs to reach index `1` before returning `false`
    [1, "2", 3, 4, 5, 6, 7, 8, 9, 10].every((el) => typeof el === "number");
  }
]); // 1
```
