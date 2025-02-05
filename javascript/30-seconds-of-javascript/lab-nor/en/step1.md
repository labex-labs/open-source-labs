# How to use Logical Nor in JavaScript

To start coding in JavaScript, access the Terminal/SSH and type `node`. Logical Nor checks if none of the given arguments are true. To return the inverse of the logical or of two values, use the logical not (`!`) operator. Here's an example:

```js
const nor = (a, b) => !(a || b);
```

And here are some outputs:

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
