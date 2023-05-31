# Checking if a String is Alphanumeric

If you want to practice coding, open the Terminal/SSH and type `node`. Here's a function that checks if a string contains only alphanumeric characters:

```js
const isAlphaNumeric = (str) => /^[a-z0-9]+$/gi.test(str);
```

To use it, call `isAlphaNumeric` with a string as its argument. It will return `true` if the string contains only alphanumeric characters, and `false` otherwise.

For example:

```js
isAlphaNumeric("hello123"); // true
isAlphaNumeric("123"); // true
isAlphaNumeric("hello 123"); // false (contains a space character)
isAlphaNumeric("#$hello"); // false (contains non-alphanumeric characters)
```

The `RegExp.prototype.test()` method is used to check if the input string matches against the alphanumeric pattern, which is represented by the regular expression `/^[a-z0-9]+$/gi`. This pattern matches any sequence of one or more lowercase letters or digits, and the `g` and `i` flags make the matching case-insensitive.
