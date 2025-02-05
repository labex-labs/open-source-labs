# Checking if a Value is a Function

To check if a value is a function, you can use the `typeof` operator with the `function` primitive.

Here's an example of a function that checks if a given value is a function:

```js
const isFunction = (val) => typeof val === "function";
```

You can use it like this:

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

To start practicing coding, open the Terminal/SSH and type `node`.
