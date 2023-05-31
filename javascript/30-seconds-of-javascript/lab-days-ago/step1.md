# JavaScript function to Calculate Days Ago

Here's a JavaScript function that calculates the date of `n` days ago from today and returns it as a string in `yyyy-mm-dd` format:

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

Here's how it works:

- The `Date` constructor is used to get the current date.
- The `Math.abs()` function is used to ensure that the number of days is positive.
- The `Date.prototype.getDate()` function is used to get the day of the month for the current date.
- The `Date.prototype.setDate()` function is used to update the date accordingly.
- The resulting date is returned as a string in `yyyy-mm-dd` format using the `Date.prototype.toISOString()` function.

Example usage:

```js
daysAgo(20); // "2020-09-16" (if current date is 2020-10-06)
```
