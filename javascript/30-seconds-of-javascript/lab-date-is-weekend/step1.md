# Checking if Date is a Weekend

To check if a given date is a weekend, follow these steps:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `Date.prototype.getDay()` method to get the day of the week as a number (0-6), with Sunday being 0 and Saturday being 6.
- Check if the day is a weekend by using a modulo operator (`%`) and comparing it to 0 or 6.
- Omit the argument, `d`, to use the current date as default.

Here's an example code snippet that you can use:

```js
const isWeekend = (d = new Date()) => d.getDay() % 6 === 0;
```

To test the function, simply call it without any argument:

```js
isWeekend(); // true or false (depending on the current date)
```

This will return `true` if the current date is a weekend (Saturday or Sunday) and `false` otherwise.
