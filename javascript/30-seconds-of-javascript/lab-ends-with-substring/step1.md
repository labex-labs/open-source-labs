# String Ends With Substring

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if a given string ends with a substring of another string.

- Use a `for...in` loop and `String.prototype.slice()` to get each substring of the given `word`, starting at the end.
- Use `String.prototype.endsWith()` to check the current substring against the `text`.
- Return the matching substring, if found. Otherwise, return `undefined`.

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

```js
endsWithSubstring('Lorem ipsum dolor sit amet<br /', '<br />'); // '<br /'
```
