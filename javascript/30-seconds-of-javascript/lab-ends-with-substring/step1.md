# A Function to Check if a String Ends with a Substring

To check if a given string ends with a substring of another string, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use a `for...in` loop and `String.prototype.slice()` to get each substring of the given `word`, starting at the end.
3. Use `String.prototype.endsWith()` to check the current substring against the `text`.
4. Return the matching substring, if found. Otherwise, return `undefined`.

Here's the code snippet to implement the above steps:

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

You can test the function with the following example:

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
