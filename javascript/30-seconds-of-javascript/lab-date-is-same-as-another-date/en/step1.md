# Checking if Two Dates are the Same

To check if two dates are the same, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Date.prototype.toISOString()` and strict equality checking (`===`) to compare the two dates.
3. Here's an example code snippet:

```js
const isSameDate = (dateA, dateB) =>
  dateA.toISOString() === dateB.toISOString();
```

4. Test the function with two dates as arguments to see if they are the same:

```js
isSameDate(new Date(2010, 10, 20), new Date(2010, 10, 20)); // true
```

This function checks whether the two dates are the same by comparing their ISO string representations.
