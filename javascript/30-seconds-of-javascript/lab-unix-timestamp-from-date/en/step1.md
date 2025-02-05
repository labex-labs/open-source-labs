# How to Get Unix Timestamp From Date in JavaScript

To get started with coding, open the Terminal/SSH and type `node`.

You can use the following steps to get the Unix timestamp from a `Date` object in JavaScript:

1. Use `Date.prototype.getTime()` to get the timestamp in milliseconds.
2. Divide the timestamp by `1000` to get the timestamp in seconds.
3. Use `Math.floor()` to round the resulting timestamp to an integer.
4. If you omit the `date` argument, the current date will be used.

Here's an example code snippet:

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

You can call the `getTimestamp()` function to get the Unix timestamp. For example:

```js
getTimestamp(); // 1602162242
```
