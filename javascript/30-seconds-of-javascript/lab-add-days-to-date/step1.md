# Function to Add Days to a Date

Here's a function that can calculate the date of `n` days from the given date and return its string representation.

To use the function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Date` constructor to create a `Date` object from the first argument.
3. Use `Date.prototype.getDate()` and `Date.prototype.setDate()` to add `n` days to the given date.
4. Use `Date.prototype.toISOString()` to return a string in `yyyy-mm-dd` format.

Here's the code for the function:

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

You can test the function using the following examples:

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
