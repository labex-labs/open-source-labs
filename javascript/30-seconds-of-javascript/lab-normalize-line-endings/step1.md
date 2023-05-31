# Function to Normalize Line Endings

To normalize line endings in a string, you can use the following function.

```js
const normalizeLineEndings = (str, normalized = "\r\n") =>
  str.replace(/\r?\n/g, normalized);
```

- Use `String.prototype.replace()` with a regular expression to match and replace line endings with the `normalized` version.
- By default, the `normalized` version is set to `'\r\n'`.
- To use a different `normalized` version, pass it as the second argument.

Here are some examples:

```js
normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n");
// 'This\r\nis a\r\nmultiline\r\nstring.\r\n'

normalizeLineEndings("This\r\nis a\nmultiline\nstring.\r\n", "\n");
// 'This\nis a\nmultiline\nstring.\n'
```
