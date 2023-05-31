# Function to Check if a String is Alpha

To check if a string contains only alphabetic characters:

- Open the Terminal/SSH and type `node` to start practicing coding.
- Use `RegExp.prototype.test()` to check if the given string matches against the alphabetic regexp pattern.
- The function `isAlpha` takes a string as an argument and returns `true` if the string contains only alphabetic characters, and `false` otherwise.

Here's an example:

```js
const isAlpha = (str) => /^[a-zA-Z]*$/.test(str);
```

```js
isAlpha("sampleInput"); // true
isAlpha("this Will fail"); // false
isAlpha("123"); // false
```
