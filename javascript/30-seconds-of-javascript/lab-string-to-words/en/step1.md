# Function to Convert String into an Array of Words

To convert a given string into an array of words, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `String.prototype.split()` method with a supplied `pattern` (defaults to non-alpha as a regexp) to convert to an array of strings.
3. Use the `Array.prototype.filter()` method to remove any empty strings.
4. Omit the second argument, `pattern`, to use the default regexp.

Here's a function that implements these steps:

```js
const words = (str, pattern = /[^a-zA-Z-]+/) =>
  str.split(pattern).filter(Boolean);
```

You can use the `words()` function with different strings to convert them into arrays of words:

```js
words("I love javaScript!!"); // ['I', 'love', 'javaScript']
words("python, javaScript & coffee"); // ['python', 'javaScript', 'coffee']
```
