# Checking for Whitespace in a String

To check if a string contains whitespace characters, follow the steps below:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `RegExp.prototype.test()` with an appropriate regular expression to check if the given string contains any whitespace characters.
- Here's an example code snippet:

  ```js
  const containsWhitespace = (str) => /\s/.test(str);
  ```

- To test the function, call `containsWhitespace` with a string as an argument. It will return `true` if the string contains whitespace characters, otherwise `false`.

  ```js
  containsWhitespace("lorem"); // false
  containsWhitespace("lorem ipsum"); // true
  ```
