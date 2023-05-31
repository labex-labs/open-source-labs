# Check if a Date is a Weekday

To check if a given date is a weekday, you can use the following code snippet:

```js
const isWeekday = (date = new Date()) => date.getDay() % 6 !== 0;
```

- This function uses `Date.prototype.getDay()` to get the day of the week as a number (0-6), where Sunday is 0 and Saturday is 6.
- It then checks if the day of the week is not equal to 0 (Sunday) or 6 (Saturday), which means it is a weekday.
- If no date is provided as an argument, the current date is used as the default.

Example usage:

```js
isWeekday(); // true (if current date is a weekday)
isWeekday(new Date(2021, 5, 28)); // true (if date is a weekday)
```
