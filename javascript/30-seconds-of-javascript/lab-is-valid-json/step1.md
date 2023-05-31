# Check If A String Is Valid JSON

To check if a given string is valid JSON, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `JSON.parse()` method and a `try...catch` block to check if the provided string is valid JSON.
3. If the string is valid, return `true`. Otherwise, return `false`.

Here's an example code snippet that implements this logic:

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

You can test this function with different input strings, like this:

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

In the last example, `null` is not a valid JSON string, so the function returns `false`.
