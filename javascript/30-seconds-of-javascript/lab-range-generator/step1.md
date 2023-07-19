# Range Generator

To generate a range of values using a given step, use the following `rangeGenerator` function. Open the Terminal/SSH and type `node` to start coding.

- Use a `while` loop and `yield` to return each value, starting from `start` and ending at `end`.
- If you want to use a default step of `1`, omit the third argument.

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

Here's an example of how to use the `rangeGenerator` function:

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// Logs 6, 7, 8, 9
```
