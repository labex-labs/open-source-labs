# JavaScript Function to Calculate Date Difference in Hours

To calculate the difference between two dates in hours using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.

2. Use the following JavaScript function to get the difference (in hours) between two `Date` objects:

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. Call the function with the two dates as arguments to get the difference in hours:

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
