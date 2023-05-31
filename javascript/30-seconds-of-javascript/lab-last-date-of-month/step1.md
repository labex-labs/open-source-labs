# Function to Return the Last Date of a Month

To get started with coding, open the Terminal/SSH and type `node`.

This function returns the last date of the month for the given date.

To achieve this, follow these steps:

1. Use `Date.prototype.getFullYear()` and `Date.prototype.getMonth()` to get the current year and month from the given date.
2. Create a new date with the given year and month incremented by `1`, and the day set to `0` (last day of previous month). You can use the `Date` constructor for this purpose.
3. If no argument is passed to the function, it will use the current date by default.
4. Return the last date of the month in the format of a string representation of the date.

Here is the code for the function:

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

You can test the function by calling it with a date object like this:

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
