# How to Get the Day of the Year in JavaScript using Date Object

To get the day of the year (number between 1-366) from a `Date` object in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Date` constructor and `Date.prototype.getFullYear()` to get the first day of the year as a `Date` object.
3. Subtract the first day of the year from the `date` object and divide by the milliseconds in each day to get the result.
4. Use `Math.floor()` to round the resulting day count to an integer.

Here's the code:

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

To test the function, call `dayOfYear()` with a `Date` object as the argument:

```js
dayOfYear(new Date()); // 272
```
