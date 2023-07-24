# Function to Calculate the Date of 'n' Days from Today

To calculate the date 'n' days from today, follow these steps:

- Open the Terminal/SSH and type 'node' to start practicing coding.
- Use the `Date` constructor to get the current date.
- Use `Math.abs()` and `Date.prototype.getDate()` to update the date accordingly.
- Set the result using `Date.prototype.setDate()`.
- Use `Date.prototype.toISOString()` to return a string in `yyyy-mm-dd` format.

Here's the code:

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

Example usage:

```js
daysFromNow(5); // Output: 2020-10-13 (if current date is 2020-10-08)
```
