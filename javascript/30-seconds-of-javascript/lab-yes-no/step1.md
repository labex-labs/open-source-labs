# Function to Check Yes/No String

To check if a string is a `'yes'` or `'no'` answer, use the following function in the Terminal/SSH by typing `node`:

```js
const yesNo = (val, def = false) =>
  /^(y|yes)$/i.test(val) ? true : /^(n|no)$/i.test(val) ? false : def;
```

- The function returns `true` if the string is `'y'`/`'yes'` and `false` if the string is `'n'`/`'no'`.
- To set a default answer, omit the second argument `def`. By default, the function will return `false`.
- The function uses `RegExp.prototype.test()` to check if the string matches `'y'`/`'yes'` or `'n'`/`'no'`.

Example usage:

```js
yesNo("Y"); // true
yesNo("yes"); // true
yesNo("No"); // false
yesNo("Foo", true); // true
```
