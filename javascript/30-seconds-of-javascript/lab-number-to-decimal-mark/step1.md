# How to Convert a Number to Decimal Mark Format

To convert a number to decimal mark format, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Number.prototype.toLocaleString()` to convert the number to decimal mark format.
3. The following code can be used for this process:

```js
const toDecimalMark = (num) => num.toLocaleString("en-US");
```

Here's an example of how to use this function:

```js
toDecimalMark(12305030388.9087); // '12,305,030,388.909'
```

This will convert the number `12305030388.9087` to the decimal mark formatted string `'12,305,030,388.909'`.
