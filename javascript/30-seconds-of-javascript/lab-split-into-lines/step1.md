# How to Start Practicing Coding in Terminal/SSH

To start practicing coding in Terminal/SSH, simply type `node`.

# Splitting a Multiline String into an Array of Lines

To split a multiline string into an array of lines:

- Use `String.prototype.split()` and a regular expression to match line breaks and create an array.
- The regular expression `/\r?\n/` matches both `\r` and `\n` line breaks.
- This will return an array of lines.

```js
const splitLines = (str) => str.split(/\r?\n/);
```

```js
splitLines("This\nis a\nmultiline\nstring.\n");
// ['This', 'is a', 'multiline', 'string.' , '']
```
