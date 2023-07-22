# How to Mask a Value in JavaScript

To mask a value in JavaScript, you can use the `mask()` function. Follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `String.prototype.slice()` to grab the portion of the characters that will remain unmasked.
3. Use `String.prototype.padStart()` to fill the beginning of the string with the `mask` character up to the original length.
4. If you want to exclude characters from the end of the string, use a negative value for `num`.
5. If you don't specify a value for `num`, the function will default to keeping the last 4 characters unmasked.
6. If you don't specify a value for `mask`, the function will default to using the `'*'` character for the mask.

Here's the code for the `mask()` function:

```js
const mask = (cc, num = 4, mask = "*") =>
  `${cc}`.slice(-num).padStart(`${cc}`.length, mask);
```

And here are some examples of how to use the `mask()` function:

```js
mask(1234567890); // '******7890'
mask(1234567890, 3); // '*******890'
mask(1234567890, -4, "$"); // '$$$$567890'
```
