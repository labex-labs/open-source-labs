# Checking if a Value is Object-Like

To check if a value is object-like, follow these steps:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. Check if the provided value is not `null` and its `typeof` is equal to `'object'`.

Here's the code you can use:

```js
const isObjectLike = (val) => val !== null && typeof val === "object";
```

You can test this function with the following examples:

```js
isObjectLike({}); // true
isObjectLike([1, 2, 3]); // true
isObjectLike((x) => x); // false
isObjectLike(null); // false
```
