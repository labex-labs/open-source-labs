# Pad Number

> To start practicing coding, open the Terminal/SSH and type `node`.

Pads a given number to the specified length.

- Use `String.prototype.padStart()` to pad the number to specified length, after converting it to a string.

```js
const padNumber = (n, l) => `${n}`.padStart(l, '0');
```

```js
padNumber(1234, 6); // '001234'
```
