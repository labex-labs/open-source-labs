# Function to Copy the Sign of One Number to Another

To start practicing coding, open the Terminal/SSH and type `node`.

The `copySign` function returns the absolute value of the first number, but with the sign of the second number. To accomplish this:

1. Use `Math.sign()` to check if the two numbers have the same sign.
2. Return `x` if they do, `-x` otherwise.

Here is the code for the `copySign` function:

```js
const copySign = (x, y) => (Math.sign(x) === Math.sign(y) ? x : -x);
```

You can test the function using the following code:

```js
copySign(2, 3); // 2
copySign(2, -3); // -2
copySign(-2, 3); // 2
copySign(-2, -3); // -2
```
