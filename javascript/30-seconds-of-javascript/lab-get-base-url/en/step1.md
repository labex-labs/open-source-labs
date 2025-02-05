# Retrieving Base URL

To retrieve the base URL from a given URL, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. Use the following JavaScript function to get the current URL without any parameters or fragment identifiers:

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. Replace `url` with the URL you want to retrieve the base URL from.
5. The function will remove everything after either `'?'` or `'#'`, if found, and return the base URL.
6. Here's an example:

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
