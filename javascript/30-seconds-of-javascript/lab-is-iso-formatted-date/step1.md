# Checking if a String is in ISO Format

To check if a given string is in the simplified extended ISO format (ISO 8601), follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Date` constructor to create a `Date` object from the given string.
3. Check if the produced date object is valid using `Date.prototype.valueOf()` and `Number.isNaN()`.
4. Compare the ISO formatted string representation of the date with the original string using `Date.prototype.toISOString()`.
5. If the strings match and the date is valid, return `true`. Otherwise, return `false`.

Here is an example code snippet:

```js
const isISOString = (val) => {
  const d = new Date(val);
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

isISOString("2020-10-12T10:10:10.000Z"); // true
isISOString("2020-10-12"); // false
```

This function will return `true` if the string is in ISO format, and `false` otherwise.
