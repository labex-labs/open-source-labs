# Check if Value is Array-Like

To check if a value is array-like, follow these steps:

1. Open Terminal/SSH.
2. Type `node`.
3. Use the following code to check if the provided argument is iterable:

```js
const isArrayLike = (obj) =>
  obj != null && typeof obj[Symbol.iterator] === "function";
```

4. The function will return `true` if the provided argument is an array-like object, and `false` otherwise.
5. For example:

```js
isArrayLike([1, 2, 3]); // true
//isArrayLike(document.querySelectorAll(".className")); // true
isArrayLike("abc"); // true
isArrayLike(null); // false
```
