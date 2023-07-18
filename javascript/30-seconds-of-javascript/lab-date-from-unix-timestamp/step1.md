# How to Create a Date Object from Unix Timestamp

To create a `Date` object from a Unix timestamp, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Multiply the timestamp by `1000` to convert it to milliseconds.
3. Use the `Date` constructor to create a new `Date` object.

Here's an example code snippet:

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

You can use this function to convert a Unix timestamp to a `Date` object like this:

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
