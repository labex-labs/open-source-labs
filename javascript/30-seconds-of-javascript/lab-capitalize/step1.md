# JavaScript Function to Capitalize First Letter of a String

To capitalize the first letter of a string in JavaScript, use the following function:

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

This function uses array destructuring and `String.prototype.toUpperCase()` to capitalize the first letter of the string. The `lowerRest` argument is optional and can be set to `true` to convert the rest of the string to lowercase.

Here is an example of how to use this function:

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
