# Function to Remove Whitespaces

To remove whitespaces from a string, use the following function.

- Use `String.prototype.replace()` with a regular expression to replace all occurrences of whitespace characters with an empty string.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## Regular Expression Explained

- `/\s+/g` breaks down as:
  - `\s`: Matches any whitespace character (spaces, tabs, line breaks)
  - `+`: Matches one or more occurrences of the previous character
  - `/g`: Global flag - matches all occurrences in the string, not just the first one

## Quick Regex Reference

Common whitespace patterns:

- `\s` - matches any whitespace (space, tab, newline)
- `\t` - matches tab characters
- `\n` - matches newline characters
- `\r` - matches carriage returns
- `` (space) - matches only space characters

For example,

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// More examples:
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

To start practicing coding, open the Terminal/SSH and type `node`.
