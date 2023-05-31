# How to Escape HTML Characters in JavaScript

To escape HTML characters in JavaScript, you can use the `escapeHTML()` function. Here are the steps to follow:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.replace()` method with a regular expression that matches the characters that need to be escaped.
3. Define a dictionary object with the escaped characters for each character that needs to be replaced.
4. Use a callback function to replace each character instance with its associated escaped character using the dictionary object.

Here's an example of the `escapeHTML()` function in action:

```js
const escapeHTML = (str) =>
  str.replace(
    /[&<>'"]/g,
    (tag) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        "'": "&#39;",
        '"': "&quot;",
      }[tag] || tag)
  );

escapeHTML('<a href="#">Me & you</a>'); // returns '&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;'
```

This function will replace any special characters in the input string with their corresponding HTML entities, making it safe to use in HTML content.
