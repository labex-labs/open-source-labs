# Case-Insensitive Substring Search

To check if a string contains a substring regardless of the case, follow these steps:

- Use the `RegExp` constructor with the `'i'` flag to create a regular expression that matches the given `searchString`, ignoring the case.
- Use `RegExp.prototype.test()` to check if the string contains the substring.

Here is an example code snippet:

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

To test this function, you can run:

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
