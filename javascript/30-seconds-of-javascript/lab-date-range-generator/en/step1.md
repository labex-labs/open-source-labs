# Date Range Generator

To generate all dates in a given range using a given step, use the following code in Terminal/SSH and type `node`:

```js
const dateRangeGenerator = function* (start, end, step = 1) {
  let d = start;
  while (d < end) {
    yield new Date(d);
    d.setDate(d.getDate() + step);
  }
};
```

This creates a generator that uses a `while` loop to iterate from `start` to `end`, using `Date` constructor to return each date in the range and increments by `step` days using `Date.prototype.getDate()` and `Date.prototype.setDate()`.

To use a default value of `1` for `step`, omit the third argument.

Here's an example of how to use the `dateRangeGenerator`:

```js
[...dateRangeGenerator(new Date("2021-06-01"), new Date("2021-06-04"))];
// [ 2021-06-01, 2021-06-02, 2021-06-03 ]
```
