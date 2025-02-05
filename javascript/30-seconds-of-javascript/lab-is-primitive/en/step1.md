# Checking for Primitive Values

To practice coding, open the Terminal or SSH and type `node`. Once you've done that, you can check whether a value is primitive or not by following these steps:

1. Create an object from the value you want to check using `Object(val)`.
2. Compare the created object with the original value using the strict inequality operator `!==`.
3. If the two values are not equal, the original value is primitive.

Here's the code for the `isPrimitive` function:

```js
const isPrimitive = (val) => Object(val) !== val;
```

You can test this function with the following values:

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

If the value you want to check is primitive, the function will return `true`. Otherwise, it will return `false`.
