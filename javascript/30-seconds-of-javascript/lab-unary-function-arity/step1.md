# Understanding Unary Function Arity

To start coding, open the Terminal/SSH and type `node`.

Unary function arity refers to a function that takes only one argument, ignoring any additional arguments.

The provided function `fn` can be called with just the first argument supplied. To create a unary function, use the following code:

```js
const unary = (fn) => (val) => fn(val);
```

An example of using `unary` with `parseInt` function is shown below:

```js
["6", "8", "10"].map(unary(parseInt)); // [6, 8, 10]
```
