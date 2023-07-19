# Getting Yesterday's Date in yyyy-mm-dd Format

To get yesterday's date in `yyyy-mm-dd` format, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Date` constructor to get the current date.
3. Decrement the date by one using `Date.prototype.getDate()`.
4. Set the decremented date using `Date.prototype.setDate()`.
5. Use `Date.prototype.toISOString()` to return a string in `yyyy-mm-dd` format.
6. Call the function `yesterday()` to get yesterday's date.

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // returns "2018-10-17" (if current date is 2018-10-18)
```

By following these steps, you will be able to retrieve yesterday's date in a clear and concise manner.
