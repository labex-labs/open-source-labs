# Format Duration

To get the human-readable format of a given number of milliseconds, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Divide the `ms` with appropriate values to obtain the appropriate values for `day`, `hour`, `minute`, `second`, and `millisecond`.
3. Use `Object.entries()` with `Array.prototype.filter()` to keep only non-zero values.
4. Create the string for each value, pluralizing appropriately, using `Array.prototype.map()`.
5. Combine the values into a string using `Array.prototype.join()`.

Here's the code:

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

Here are some examples:

```js
formatDuration(1001); // '1 second, 1 millisecond'
formatDuration(34325055574);
// '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'
```
