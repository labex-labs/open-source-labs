# How to Deep Freeze an Object in JavaScript

To deep freeze an object in JavaScript, follow these steps:

1. Use `Object.keys()` to get all the properties of the passed object.
2. Iterate over the properties using `Array.prototype.forEach()`.
3. Call `Object.freeze()` recursively on all properties that are objects, applying `deepFreeze()` as necessary.
4. Finally, use `Object.freeze()` to freeze the given object.

Here's the code:

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

You can test the deep frozen object using the following code:

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // not allowed
val[1][0] = 4; // not allowed as well
```

The above code will throw an error because the `val` object is deeply frozen and cannot be modified.
