# Number Formatting Function

To format a number using the local number format order, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Number.prototype.toLocaleString()` method to convert a number to using the local number format separators.
3. Pass the number you want to format as an argument to the function.

Here's an example implementation:

```js
const formatNumber = (num) => num.toLocaleString();
```

And here are some examples of how to use the function:

```js
formatNumber(123456); // '123,456' in `en-US`
formatNumber(15675436903); // '15.675.436.903' in `de-DE`
```
