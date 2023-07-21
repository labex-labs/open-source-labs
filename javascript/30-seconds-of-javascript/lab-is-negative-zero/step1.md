# Checking for Negative Zero

To check if a number is negative zero, open the Terminal/SSH and enter `node`. Then, use the following code:

```js
const isNegativeZero = (val) => val === 0 && 1 / val === -Infinity;
```

This will check if the passed value is equal to `0` and if `1` divided by the value equals `-Infinity`. For example:

```js
isNegativeZero(-0); // true
isNegativeZero(0); // false
```
