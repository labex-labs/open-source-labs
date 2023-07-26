# Converting a Value to a Safe Integer

To convert a value to a safe integer, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Math.max()` and `Math.min()` to find the closest safe value.
3. Use `Math.round()` to convert the value to an integer.

Here's an example code snippet that demonstrates how to convert a value to a safe integer:

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

You can test this function with the following input:

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
