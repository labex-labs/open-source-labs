# Converting Object to Query String

To convert an object to a query string, use `objectToQueryString()` function which generates a query string from the key-value pairs of the given object.

The function works as follows:

- It uses `Array.prototype.reduce()` on `Object.entries()` to create the query string from `queryParameters`.
- It determines the `symbol` to be either `?` or `&` based on the length of `queryString`.
- It concatenates `val` to `queryString` only if it's a string.
- It returns the `queryString` or an empty string when the `queryParameters` are falsy.

Here's the code for `objectToQueryString()` function:

```js
const objectToQueryString = (queryParameters) => {
  return queryParameters
    ? Object.entries(queryParameters).reduce(
        (queryString, [key, val], index) => {
          const symbol = queryString.length === 0 ? "?" : "&";
          queryString +=
            typeof val === "string" ? `${symbol}${key}=${val}` : "";
          return queryString;
        },
        "",
      )
    : "";
};
```

Example usage of `objectToQueryString()` function:

```js
objectToQueryString({ page: "1", size: "2kg", key: undefined }); // returns '?page=1&size=2kg'
```
