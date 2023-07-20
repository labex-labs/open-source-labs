# Unescape HTML

This function unescapes escaped HTML characters. To use it, follow these steps:

1. Open the Terminal/SSH.
2. Type `node`.
3. Copy and paste the following code:

```js
const unescapeHTML = (str) =>
  str.replace(
    /&amp;|&lt;|&gt;|&#39;|&quot;/g,
    (tag) =>
      ({
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&#39;": "'",
        "&quot;": '"',
      }[tag] || tag)
  );
```

4. Call the `unescapeHTML` function and pass it a string with escaped characters.
5. The function will return the unescaped string.

Example usage:

```js
unescapeHTML("&lt;a href=&quot;#&quot;&gt;Me &amp; you&lt;/a&gt;");
// '<a href="#">Me & you</a>'
```
