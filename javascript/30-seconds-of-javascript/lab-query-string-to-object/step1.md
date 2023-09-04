# Converting Query String to Object

To convert a query string or URL to an object, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.split()` to extract the parameters from the given `url`.
3. Use the `URLSearchParams` constructor to create an object and convert it to an array of key-value pairs using the spread operator (`...`).
4. Use `Array.prototype.reduce()` to convert the array of key-value pairs into an object.

Here is the code to convert the query string:

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {},
  );
```

Example usage:

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
