# Convert Bytes to Human-Readable String

To convert a number in bytes to a human-readable string, use the `prettyBytes()` function. Here are some things to keep in mind:

- The function uses an array dictionary of units to be accessed based on the exponent.
- You can use the second argument, `precision`, to truncate the number to a certain number of digits. The default value is `3`.
- You can use the third argument, `addSpace`, to add space between the number and unit. The default value is `true`.
- The function returns the prettified string by building it up, taking into account the supplied options and whether it is negative or not.

Here's the code for the `prettyBytes()` function:

```js
const prettyBytes = (num, precision = 3, addSpace = true) => {
  const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  if (Math.abs(num) < 1) return num + (addSpace ? " " : "") + UNITS[0];
  const exponent = Math.min(
    Math.floor(Math.log10(num < 0 ? -num : num) / 3),
    UNITS.length - 1,
  );
  const n = Number(
    ((num < 0 ? -num : num) / 1000 ** exponent).toPrecision(precision),
  );
  return (num < 0 ? "-" : "") + n + (addSpace ? " " : "") + UNITS[exponent];
};
```

And here are some examples of using the `prettyBytes()` function:

```js
prettyBytes(1000); // '1 KB'
prettyBytes(-27145424323.5821, 5); // '-27.145 GB'
prettyBytes(123456789, 3, false); // '123MB'
```
