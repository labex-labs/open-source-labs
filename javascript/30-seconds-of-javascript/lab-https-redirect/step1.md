# How to Redirect a Page to HTTPS

To redirect a web page to HTTPS if it's currently in HTTP, follow these steps:

1. Use `location.protocol` to get the protocol currently being used.
2. If the protocol is not HTTPS, use `location.replace()` to replace the existing page with the HTTPS version of the page.
3. Use `location.href` to get the full address, split it with `String.prototype.split()` and remove the protocol part of the URL.
4. Note that pressing the back button won't take it back to the HTTP page as it's replaced in the history.

Here's an example of the code:

```js
const httpsRedirect = () => {
  if (location.protocol !== "https:")
    location.replace("https://" + location.href.split("//")[1]);
};

httpsRedirect();
// If you are on http://mydomain.com, you will be redirected to https://mydomain.com
```
