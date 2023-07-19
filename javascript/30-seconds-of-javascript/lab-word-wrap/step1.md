# Instructions for Word Wrap String

To practice coding, open the Terminal/SSH and type `node`.

This code wraps a string to a given number of characters using a string break character. To use it, follow these steps:

1. Use `String.prototype.replace()` and a regular expression to insert a given break character at the nearest whitespace of `max` characters.
2. If you don't want to use the default value of `'\n'` for the third argument, `br`, you can omit it and provide your own character.

Here is the code:

```js
const wordWrap = (str, max, br = "\n") =>
  str.replace(
    new RegExp(`(?![^\\n]{1,${max}}$)([^\\n]{1,${max}})\\s`, "g"),
    "$1" + br
  );
```

And here are some examples of how to use it:

```js
wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32
);
// 'Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nFusce tempus.'

wordWrap(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce tempus.",
  32,
  "\r\n"
);
// 'Lorem ipsum dolor sit amet,\r\nconsectetur adipiscing elit.\r\nFusce tempus.'
```
