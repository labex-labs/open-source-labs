# A Function to Indent Strings in JavaScript

To add indentation to each line in a given string, you can use the `indentString()` function in JavaScript. This function takes three arguments: `str`, `count`, and `indent`.

- The `str` argument represents the string you want to indent.
- The `count` argument determines how many times you want to indent each line.
- The `indent` argument is optional and represents the character you want to use for indentation. If you don't provide it, the default value is a single space character (`' '`).

Here is the code for the `indentString()` function:

```js
const indentString = (str, count, indent = " ") =>
  str.replace(/^/gm, indent.repeat(count));
```

To use this function, simply call it with the desired arguments. Here are some examples:

```js
indentString("Lorem\nIpsum", 2); // '  Lorem\n  Ipsum'
indentString("Lorem\nIpsum", 2, "_"); // '__Lorem\n__Ipsum'
```

In the first example, `indentString('Lorem\nIpsum', 2)` returns `'  Lorem\n  Ipsum'`, which means that each line of the input string has been indented two times with space characters.

In the second example, `indentString('Lorem\nIpsum', 2, '_')` returns `'__Lorem\n__Ipsum'`, which means that each line of the input string has been indented two times with underscore characters (`'_'`).
