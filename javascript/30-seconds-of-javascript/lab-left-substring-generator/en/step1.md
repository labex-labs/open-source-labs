# Code Practice: Left Substring Generator

To generate all left substrings of a given string, use the `leftSubstrGenerator` function provided below.

```js
const leftSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(0, i + 1);
};
```

To use the function, open the Terminal/SSH and type `node`. Then, enter the function with a string argument:

```js
[...leftSubstrGenerator("hello")];
// [ 'h', 'he', 'hel', 'hell', 'hello' ]
```

The function uses `String.prototype.length` to terminate early if the string is empty and a `for...in` loop with `String.prototype.slice()` to `yield` each substring of the given string, starting at the beginning.
