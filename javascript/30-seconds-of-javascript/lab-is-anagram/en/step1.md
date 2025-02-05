# JavaScript Function to Check if a String is Anagram

To check if a string is an anagram of another string, use the following JavaScript function. It's case-insensitive and ignores spaces, punctuation, and special characters.

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

To use the function, open the Terminal/SSH and type `node`. Then, call the function with two strings as arguments:

```js
isAnagram("iceman", "cinema"); // true
```

The function uses `String.prototype.toLowerCase()` and `String.prototype.replace()` with an appropriate regular expression to remove unnecessary characters. It also uses `String.prototype.split()`, `Array.prototype.sort()`, and `Array.prototype.join()` on both strings to normalize them and check if their normalized forms are equal.
