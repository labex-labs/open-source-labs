# How to Remove HTML/XML Tags from a String

To remove HTML/XML tags from a string, you can use a regular expression. Follow these steps:

1. Open the Terminal/SSH
2. Type `node` to start practicing coding
3. Use the following code:

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. Test the function with the following example:

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

This will remove all HTML/XML tags from the input string and return the remaining text.
