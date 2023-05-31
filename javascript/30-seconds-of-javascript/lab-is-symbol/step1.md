# Checking if a Value is a Symbol in JavaScript

To check if a value is a symbol primitive in JavaScript, you can use the `typeof` operator. Here's an example code snippet that you can use:

```js
const isSymbol = (val) => typeof val === "symbol";
```

You can call the `isSymbol` function and pass a symbol as an argument to check if it returns `true`. Here's an example:

```js
isSymbol(Symbol("x")); // true
```
