# Function to Calculate Date Difference in Seconds

To calculate the difference between two dates in seconds, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Subtract the two `Date` objects and divide by the number of milliseconds in a second.
3. The result will be the difference between the two dates in seconds.

Here's a JavaScript function that does this calculation:

```js
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

To use this function, pass in two `Date` objects as arguments, like this:

```js
getSecondsDiffBetweenDates(
  new Date("2020-12-24 00:00:15"),
  new Date("2020-12-24 00:00:17")
); // 2
```
