# Function to Calculate Date Difference in Days

To calculate the difference between two dates in days, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `getDaysDiffBetweenDates` function with two `Date` objects as arguments.
3. The function will subtract the initial date from the final date and divide the result by the number of milliseconds in a day to get the difference in days between them.

Here's the code for the `getDaysDiffBetweenDates` function:

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

To use the function, pass in two `Date` objects in the format `YYYY-MM-DD`:

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

This will return the difference between the two dates in days, which is 9 in this example.
