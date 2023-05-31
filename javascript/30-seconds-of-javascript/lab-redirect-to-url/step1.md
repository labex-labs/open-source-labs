# How to Redirect to a URL in JavaScript

To redirect to a different URL using JavaScript, you can use the `Window.location.href` or `Window.location.replace()` method. Here's how you can do it:

```js
const redirect = (url, asLink = true) =>
  asLink ? (window.location.href = url) : window.location.replace(url);
```

To use the `redirect` function, pass in the URL you want to redirect to as the first argument. You can also pass in a second argument to simulate a link click (`true` is the default) or an HTTP redirect (`false`).

Here's an example of how to use the `redirect` function:

```js
redirect("https://google.com");
```

This will redirect the user to the Google homepage.
