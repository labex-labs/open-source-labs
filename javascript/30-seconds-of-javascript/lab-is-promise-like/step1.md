# JavaScript Promises

To check if an object is similar to a Promise, use the function `isPromiseLike`. This function checks if the object is not null, has a type of object or function, and has a `.then` property that is also a function.

Here is the code for `isPromiseLike`:

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

Here are some examples of how to use `isPromiseLike`:

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

To start practicing coding in JavaScript, open the Terminal/SSH and type `node`.
