# Object with URL Parameters

To create an object that contains the parameters of the current URL, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.match()` with an appropriate regular expression to extract all the key-value pairs.
3. Use `Array.prototype.reduce()` to map and combine them into a single object.
4. Pass `location.search` as the argument to apply to the current URL.

Here is the code:

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)), a
    ),
    {},
  );
```

You can use this function with any URL to get an object with its parameters. Here are some examples:

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam', surname: 'Smith'}
```
