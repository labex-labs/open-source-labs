# How to Serialize a Cookie

To start practicing coding, open the Terminal/SSH and type `node`. Then, follow these steps to serialize a cookie name-value pair into a Set-Cookie header string:

1. Use template literals and `encodeURIComponent()` to create the appropriate string.
2. Implement the `serializeCookie` function by passing in the `name` and `val` parameters.
3. The function will return a string that is properly serialized.

Here is an example of how to use the `serializeCookie` function:

```js
const serializeCookie = (name, val) =>
  `${encodeURIComponent(name)}=${encodeURIComponent(val)}`;

serializeCookie("foo", "bar"); // 'foo=bar'
```

In this example, the `serializeCookie` function takes in `foo` as the cookie name and `bar` as the cookie value, and returns a serialized cookie string of `foo=bar`.
