# Function to Add Business Days to a Given Date

To calculate a future date by adding a given number of business days, you can use the `addWeekDays` function. Here are the steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `addWeekDays` function that takes two arguments: `startDate` and `count`.
3. `startDate` is the date from which you want to start adding business days.
4. `count` is the number of business days you want to add to the start date.
5. The function constructs an array using `Array.from()` method and sets the length equal to the `count` of business days to be added.
6. `Array.prototype.reduce()` method is used to iterate over the array, starting from `startDate`, and incrementing it using `Date.prototype.getDate()` and `Date.prototype.setDate()`.
7. The function checks whether the current `date` is on a weekend or not.
8. If the current `date` is on a weekend, the function updates it again by adding either one day or two days to make it a weekday.
9. The function does not take official holidays into account.

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

Here are some examples of how you can use the `addWeekDays` function:

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
