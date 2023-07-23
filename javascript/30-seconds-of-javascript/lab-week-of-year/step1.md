# Obtaining the Week of Year from a Date in JavaScript

To obtain the zero-indexed week of the year that corresponds to a date in JavaScript, follow these steps:

1. Create a `weekOfYear` function that takes a `date` parameter.
2. Use the `Date` constructor and `Date.prototype.getFullYear()` to get the first day of the year as a `Date` object.
3. Use `Date.prototype.setDate()`, `Date.prototype.getDate()` and `Date.prototype.getDay()` along with the modulo (`%`) operator to get the first Monday of the year.
4. Subtract the first Monday of the year from the given `date` and divide with the number of milliseconds in a week.
5. Use `Math.round()` to get the zero-indexed week of the year corresponding to the given `date`.
6. If the given `date` is before the first Monday of the year, `-0` is returned.

Here's the code:

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

To use the `weekOfYear` function, simply call it with a `Date` object as its parameter:

```js
weekOfYear(new Date("2021-06-18")); // 23
```

This will return the zero-indexed week of the year that corresponds to the given date, which in this case is `23`.
