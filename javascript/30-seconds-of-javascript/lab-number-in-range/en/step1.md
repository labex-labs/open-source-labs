# Function to Check if a Number is Within a Given Range

To check if a number falls within a specified range, use the `inRange` function. Begin by opening the Terminal/SSH and typing `node` to start coding.

Here are the steps to use the `inRange` function:

1. Use arithmetic comparison to check if the given number is in the specified range.
2. If the second argument, `end`, is not specified, the range is considered to be from `0` to `start`.
3. The `inRange` function takes three arguments: `n`, `start`, and `end`.
4. If `end` is less than `start`, the function swaps the values of `start` and `end`.
5. If `end` is not specified, the function checks if `n` is greater than or equal to 0 and less than `start`.
6. If `end` is specified, the function checks if `n` is greater than or equal to `start` and less than `end`.
7. The function returns `true` if `n` is within the specified range, and `false` otherwise.

Here is the `inRange` function:

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

Here are some examples of how to use the `inRange` function:

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
