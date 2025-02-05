# Count Weekdays Between Two Dates

To count the weekdays between two dates, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.from()` to create an array with a length equal to the number of days between `startDate` and `endDate`.
3. Use `Array.prototype.reduce()` to iterate over the array, checking if each date is a weekday and incrementing `count`.
4. Update `startDate` with the next day each loop using `Date.prototype.getDate()` and `Date.prototype.setDate()` to advance it by one day.
5. Please note that this function does not take official holidays into account.

Here's the code to implement this:

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

You can use the following code to test the function:

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
