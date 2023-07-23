# Checking if a Value is a String

To check if a value is a string, use the `typeof` keyword followed by the value you want to check. This method only works for string primitives.

Here's an example code that checks if a given value is a string:

```js
const isString = (val) => typeof val === "string";
```

You can use the `isString` function like this:

```js
isString("10"); // true
```
