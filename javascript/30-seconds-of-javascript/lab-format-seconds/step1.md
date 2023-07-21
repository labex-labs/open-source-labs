# Function to Format Seconds as ISO Time

To use this code, open the Terminal/SSH and type `node`. This function takes a number of seconds as an argument and returns the ISO time format. Here's how it works:

- Divide the number of seconds by the appropriate values to obtain the corresponding values for `hour`, `minute` and `second`.
- Store the sign of the number in a variable to prepend it to the result.
- Use `Array.prototype.map()` in combination with `Math.floor()` and `String.prototype.padStart()` to stringify and format each segment.
- Use `Array.prototype.join()` to combine the values into a string.

Here's the code:

```js
const formatSeconds = (s) => {
  const [hour, minute, second, sign] =
    s > 0
      ? [s / 3600, (s / 60) % 60, s % 60, ""]
      : [-s / 3600, (-s / 60) % 60, -s % 60, "-"];

  return (
    sign +
    [hour, minute, second]
      .map((v) => `${Math.floor(v)}`.padStart(2, "0"))
      .join(":")
  );
};
```

You can test the function with these examples:

```js
formatSeconds(200); // '00:03:20'
formatSeconds(-200); // '-00:03:20'
formatSeconds(99999); // '27:46:39'
```
