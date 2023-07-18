# JavaScript Function to Check if a String is Lowercase

To check if a given string is lowercase, you can use the following JavaScript function. First, convert the string to lowercase using `String.prototype.toLowerCase()` and then compare it to the original string using strict equality (`===`).

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

Here's an example usage:

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

To use this function, open the Terminal/SSH and type `node`.
