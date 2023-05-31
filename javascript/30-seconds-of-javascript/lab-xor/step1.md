# Logical Xor

To start practicing coding, open the Terminal/SSH and type `node`. The logical xor checks if only one of the arguments is `true`. To create the logical xor, use the logical or (`||`), and (`&&`), and not (`!`) operators on the two given values. Here's an example code for the same:

```js
const xor = (a, b) => (a || b) && !(a && b);
```

Here are the output values:

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
