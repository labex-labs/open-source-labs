# How to Pad a Number in JavaScript

To pad a number in JavaScript, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `String.prototype.padStart()` method to pad the number to the specified length, after converting it to a string.
3. The `padNumber()` function below demonstrates this approach.
4. Pass the number and the desired length as arguments to the function.
5. The function returns the padded number as a string.

```js
const padNumber = (n, l) => `${n}`.padStart(l, "0");
```

Example usage:

```js
padNumber(1234, 6); // '001234'
```
