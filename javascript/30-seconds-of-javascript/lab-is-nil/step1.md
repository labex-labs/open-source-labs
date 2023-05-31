# How to Check if a Value is Null or Undefined in JavaScript

To determine if a value is `null` or `undefined` in JavaScript, you can use the strict equality operator (`===`). Here's an example code snippet that checks if the specified value is `null` or `undefined`:

```js
const isNil = (val) => val === undefined || val === null;
```

You can use this function to check if a value is `null` or `undefined`, like this:

```js
isNil(null); // true
isNil(undefined); // true
isNil(""); // false
```

To start practicing coding in JavaScript, you can open the Terminal/SSH and type `node`.
