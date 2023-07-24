# URL Segments Joining and Normalization

To join given URL segments together and normalize the resulting URL, follow the steps below:

1. Use `Array.prototype.join()` to combine URL segments.
2. Use a series of `String.prototype.replace()` calls with various regular expressions to normalize the resulting URL by:
   - Removing double slashes
   - Adding proper slashes for the protocol
   - Removing slashes before parameters
   - Combining parameters with `'&'` and normalizing the first parameter delimiter.

Use the code snippet below to join and normalize URL segments:

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

Example usage:

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
