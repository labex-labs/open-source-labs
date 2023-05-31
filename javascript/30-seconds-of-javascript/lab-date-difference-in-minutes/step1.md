# Function to Calculate Date Difference in Minutes

To calculate the difference (in minutes) between two dates, use the following function:

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

Simply subtract the two `Date` objects and divide by the number of milliseconds in a minute to get the difference (in minutes) between them.

Here's an example usage of the function:

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

To start practicing coding, open the Terminal/SSH and type `node`.
