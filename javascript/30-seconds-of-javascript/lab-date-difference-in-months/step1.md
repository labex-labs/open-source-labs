# Function to Calculate Date Difference in Months

To calculate the difference between two dates in months, use the following function:

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0,
  );
```

To use this function, pass two `Date` objects as arguments. For example:

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

This function uses the `Date.prototype.getFullYear()` and `Date.prototype.getMonth()` methods to calculate the difference in months between two dates.
