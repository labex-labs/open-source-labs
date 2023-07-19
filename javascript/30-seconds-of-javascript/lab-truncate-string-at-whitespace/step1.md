# How to Truncate a String at Whitespace in JavaScript

To practice coding, open the Terminal/SSH and type `node`.

Here's a function that truncates a string up to a specified length while respecting whitespace whenever possible:

```js
const truncateStringAtWhitespace = (str, lim, ending = "...") => {
  if (str.length <= lim) return str;
  const lastSpace = str.slice(0, lim - ending.length + 1).lastIndexOf(" ");
  return str.slice(0, lastSpace > 0 ? lastSpace : lim - ending.length) + ending;
};
```

To use this function, pass in the string you want to truncate as the first argument, the maximum length as the second argument, and an optional ending string as the third argument. If the length of the string is less than or equal to the specified limit, the original string will be returned. Otherwise, the function will find the last space before the limit and truncate the string at that point, adding the ending string if specified.

Here are some examples:

```js
truncateStringAtWhitespace("short", 10); // 'short'
truncateStringAtWhitespace("not so short", 10); // 'not so...'
truncateStringAtWhitespace("trying a thing", 10); // 'trying...'
truncateStringAtWhitespace("javascripting", 10); // 'javascr...'
```
