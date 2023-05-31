# Check If a Number Is a Power of Two

To check if a number is a power of two, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the bitwise binary AND operator (`&`) to determine if the number (`n`) is a power of `2`.
3. Additionally, check that `n` is not falsy.
4. The following code functionally checks if `n` is a power of two:

```js
const isPowerOfTwo = (n) => !!n && (n & (n - 1)) == 0;
```

Here are some examples of how to use the `isPowerOfTwo` function:

```js
isPowerOfTwo(0); // false
isPowerOfTwo(1); // true
isPowerOfTwo(8); // true
```
