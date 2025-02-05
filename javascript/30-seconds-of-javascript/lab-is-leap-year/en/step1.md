# Code for Checking Leap Year

To check if a given `year` is a leap year, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start coding.
3. Use the `Date` constructor and set the date to February 29th of the given `year`.
4. Check if the month is equal to `1` using `Date.prototype.getMonth()`.
5. Use the following code snippet to check if a year is a leap year:

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

Here is an example of how to use this code:

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
