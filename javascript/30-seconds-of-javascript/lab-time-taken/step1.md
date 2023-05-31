# Measuring Time Taken by a Function

To measure the time taken by a function, use `console.time()` and `console.timeEnd()` to determine the difference between the start and end times.

Here's an example function called `timeTaken` that measures the time taken by a callback function:

```js
const timeTaken = (callback) => {
  console.time("timeTaken");
  const result = callback();
  console.timeEnd("timeTaken");
  return result;
};
```

To use this function, simply pass in your callback as an argument. For example:

```js
timeTaken(() => Math.pow(2, 10)); // Returns 1024, and logs: timeTaken: 0.02099609375ms
```

In the example above, the `timeTaken` function is used to measure the time taken to execute the `Math.pow(2, 10)` function call, which returns 1024. The console output will show the time taken in milliseconds (ms).
