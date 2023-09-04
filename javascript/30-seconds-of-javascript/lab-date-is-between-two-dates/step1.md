# Checking if a Date is Between Two Dates

To check if a date is between two other dates, use the greater than (`>`) and less than (`<`) operators in JavaScript. Here's an example function:

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

To use this function, pass in the start date, end date, and date to check. The function will return `true` if the date is between the start and end dates, and `false` otherwise. Here are some examples:

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19),
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25),
); // true
```

To start practicing coding, open the Terminal/SSH and type `node`.
