# Obtaining Tomorrow's Date

To practice coding, you may begin by opening the Terminal/SSH and typing `node`. Once you have done this, you can obtain tomorrow's date with the following steps:

1. Use the `Date` constructor to get the current date.
2. Increment it by one using `Date.prototype.getDate()`.
3. Set the value to the result using `Date.prototype.setDate()`.
4. Use `Date.prototype.toISOString()` to return a string in `yyyy-mm-dd` format.

Here is the code you can use:

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

Once you have entered this code, you can obtain tomorrow's date by calling the function `tomorrow()`. For example, if today's date is 2018-10-18, the output will be `2018-10-19`.
