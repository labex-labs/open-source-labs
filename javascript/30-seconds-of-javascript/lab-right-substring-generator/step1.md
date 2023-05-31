# Right Substring Generator

To generate all right substrings of a given string, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.length` to stop the iteration early if the string is empty.
3. Use a `for...in` loop and `String.prototype.slice()` to `yield` each substring of the given string, starting from the end.

Here's the code snippet:

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

Example usage:

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
