# Function to Check if a String is an Absolute URL

To check if a given string is an absolute URL, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `RegExp.prototype.test()` to test if the string is an absolute URL.
3. The function should be defined as `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);`
4. The function takes a string argument `str` and returns `true` if the string is an absolute URL, and `false` otherwise.
5. Test the function using the examples provided:

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
