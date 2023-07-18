# Function to Determine Quarter of Year

To determine the quarter of the year, use the `quarterOfYear()` function. This function takes an optional `date` argument and returns an array with the quarter and year to which the supplied date belongs.

To use this function, open the Terminal/SSH and type `node`. Then, copy and paste the following code:

```js
const quarterOfYear = (date = new Date()) => [
  Math.ceil((date.getMonth() + 1) / 3),
  date.getFullYear(),
];
```

The `quarterOfYear()` function uses the following steps to calculate the quarter and year:

- Uses `Date.prototype.getMonth()` to get the current month in the range (0, 11), adds `1` to map it to the range (1, 12).
- Uses `Math.ceil()` and divides the month by `3` to get the current quarter.
- Uses `Date.prototype.getFullYear()` to get the year from the given `date`.
- Omits the argument, `date`, to use the current date by default.

Here are some examples of how to use the `quarterOfYear()` function:

```js
quarterOfYear(new Date("07/10/2018")); // [ 3, 2018 ]
quarterOfYear(); // [ 4, 2020 ]
```
