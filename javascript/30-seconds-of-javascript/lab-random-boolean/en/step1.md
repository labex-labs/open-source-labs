# How to Generate a Random Boolean Value in JavaScript

To generate a random boolean value in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Math.random()` method to generate a random number.
3. Check if the random number is greater than or equal to `0.5`.
4. Return `true` if the number is greater than or equal to `0.5`, otherwise return `false`.

Here's a concise implementation of the code:

```js
const randomBoolean = () => Math.random() >= 0.5;
```

You can test the function by calling `randomBoolean()` which will return either `true` or `false`.
