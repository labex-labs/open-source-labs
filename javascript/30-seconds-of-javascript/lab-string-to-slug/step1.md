# Function to Convert String to URL Slug

To convert a string to a slug that can be used in a URL, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `String.prototype.toLowerCase()` and `String.prototype.trim()` methods to normalize the string.
3. Use the `String.prototype.replace()` method to replace spaces, dashes, and underscores with `-`, and remove special characters.
4. Implement the following code:

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. Test the function with the input `slugify('Hello World!');` and it should return the output `'hello-world'`.
