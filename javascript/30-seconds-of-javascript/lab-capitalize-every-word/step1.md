# How to Capitalize Every Word in JavaScript

To capitalize every word in a string using JavaScript, you can use the `String.prototype.replace()` method to match the first character of each word, and then use the `String.prototype.toUpperCase()` method to capitalize it.

Here's an example code snippet you can use:

```js
const capitalizeEveryWord = (str) =>
  str.replace(/\b[a-z]/g, (char) => char.toUpperCase());
```

To use this function, pass in the string you want to capitalize as an argument, like this:

```js
capitalizeEveryWord("hello world!"); // 'Hello World!'
```

This will return the capitalized string 'Hello World!'.
