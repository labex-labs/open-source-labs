# Matching Object Properties with a Function

To start practicing coding, open the Terminal/SSH and type `node`.

This function compares two objects and checks if the first object contains equivalent property values to the second one. It does so based on a provided function.

To use this function, follow these steps:

- Use `Object.keys()` to retrieve all the keys of the second object.
- Use `Array.prototype.every()`, `Object.prototype.hasOwnProperty()`, and the provided function to determine if all keys exist in the first object and have equivalent values.
- If no function is provided, the values will be compared using the equality operator.

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key],
  );
```

Here is an example of how to use this function:

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV),
); // true
```

This example checks if the two objects have equivalent values for the `greeting` property. It uses the `isGreeting` function to ensure that both values are valid greetings.
