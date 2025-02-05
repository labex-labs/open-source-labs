# JavaScript Function to Get Number of Days in a Month

To find the number of days in a specific month of a given year using JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Create a function named `daysInMonth` that takes two parameters: `year` and `month`.
3. Inside the `daysInMonth` function, use the `Date` constructor to create a date object from the given `year` and `month`.
4. Set the days parameter to `0` to get the last day of the previous month, since months are zero-indexed.
5. Use `Date.prototype.getDate()` to return the number of days in the given `month`.
6. Return the number of days from the `daysInMonth` function.

Here's the JavaScript code for the `daysInMonth` function:

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

You can use the `daysInMonth` function to get the number of days in any month of any year, as shown in these examples:

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
