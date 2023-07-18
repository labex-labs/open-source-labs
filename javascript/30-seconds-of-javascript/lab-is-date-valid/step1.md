# How to Check if a Date Is Valid

To check if a date is valid, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the spread operator (`...`) to pass the array of arguments to the `Date` constructor.
3. Use `Date.prototype.valueOf()` and `Number.isNaN()` to check if a valid `Date` object can be created from the given values.

Here's an example code snippet:

```js
const isDateValid = (...val) => !Number.isNaN(new Date(...val).valueOf());
```

You can test the function with different values, as shown below:

```js
isDateValid("December 17, 1995 03:24:00"); // true
isDateValid("1995-12-17T03:24:00"); // true
isDateValid("1995-12-17 T03:24:00"); // false
isDateValid("Duck"); // false
isDateValid(1995, 11, 17); // true
isDateValid(1995, 11, 17, "Duck"); // false
isDateValid({}); // false
```
