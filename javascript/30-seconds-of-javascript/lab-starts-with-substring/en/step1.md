# Function to Check If String Starts With Substring

To check if a given string starts with a substring of another string, follow the steps below:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use a `for...in` loop and the `String.prototype.slice()` method to get each substring of the given `word`, starting at the beginning.
- Use the `String.prototype.startsWith()` method to check the current substring against the `text`.
- If a matching substring is found, return it. Otherwise, return `undefined`.

Here's a JavaScript function that does this:

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

You can call this function as follows:

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // returns '/>'
```
