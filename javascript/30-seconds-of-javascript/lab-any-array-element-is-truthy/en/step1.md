# Testing if Any Array Element is Truthy

To start practicing coding, open the Terminal/SSH and type `node`.

To check if any element in a collection returns `true` based on a provided function, use `Array.prototype.some()`. If you want to use the `Boolean` function as default, you may omit the second argument, `fn`.

Here is an example code:

```js
const any = (arr, fn = Boolean) => arr.some(fn);
```

You can test it using the following examples:

```js
any([0, 1, 2, 0], (x) => x >= 2); // true
any([0, 0, 1, 0]); // true
```
