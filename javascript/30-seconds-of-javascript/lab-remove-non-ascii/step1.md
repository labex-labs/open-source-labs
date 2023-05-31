# How to Remove Non-ASCII Characters in JavaScript

To remove non-printable ASCII characters in JavaScript, you can follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `String.prototype.replace()` method with a regular expression to remove non-printable ASCII characters.
3. The regular expression `/[^\x20-\x7E]/g` matches any character that is not in the printable ASCII range (decimal values 32 to 126).
4. The `g` flag is used to perform a global match (i.e., replace all occurrences of non-ASCII characters in the string).
5. Here's an example of how to use the `removeNonASCII` function:

```js
const removeNonASCII = (str) => str.replace(/[^\x20-\x7E]/g, "");

removeNonASCII("äÄçÇéÉêlorem-ipsumöÖÐþúÚ"); // 'lorem-ipsum'
```

This will return the string with all non-ASCII characters removed.
