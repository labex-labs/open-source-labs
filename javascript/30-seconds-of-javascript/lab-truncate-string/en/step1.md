# Truncate a String in JavaScript

To truncate a string in JavaScript, you can use the `truncateString` function. This function takes two arguments: `str` (the string to be truncated) and `num` (the maximum length of the truncated string).

The `truncateString` function checks if the length of the `str` is greater than `num`. If it is, the function truncates the string to the desired length and appends `'...'` to the end. If not, it returns the original string.

Here's the code for the `truncateString` function:

```js
const truncateString = (str, num) =>
  str.length > num ? str.slice(0, num > 3 ? num - 3 : num) + "..." : str;
```

And here's an example of how to use the `truncateString` function:

```js
truncateString("boomerang", 7); // 'boom...'
```
