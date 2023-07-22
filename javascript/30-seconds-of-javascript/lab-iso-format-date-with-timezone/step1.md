# Converting Dates to ISO Format with Timezone

To convert a date to the extended ISO format (ISO 8601), including the timezone offset, follow these steps:

1. Open the Terminal/SSH and enter `node` to begin coding.
2. Use `Date.prototype.getTimezoneOffset()` to get the timezone offset and reverse it. Store its sign in `diff`.
3. Define a helper function, `pad()`, that normalizes any passed number to an integer using `Math.floor()` and `Math.abs()` and pads it to `2` digits, using `String.prototype.padStart()`.
4. Use `pad()` and the built-in methods in the `Date` prototype to build the ISO 8601 string with timezone offset.

Here's the code you can use:

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

Use the function `toISOStringWithTimezone()` with a `new Date()` object as the argument to get the date in ISO format with timezone offset. For example:

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
