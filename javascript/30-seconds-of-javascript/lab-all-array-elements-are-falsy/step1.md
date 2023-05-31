# Function to Test if All Array Elements Are Falsy

To test if all elements in an array are falsy, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Array.prototype.some()` to test if any elements in the collection return `true` based on the provided predicate function.
3. If you omit the second argument, `fn`, the function will use `Boolean` as a default.
4. The function returns `true` if all elements in the array are falsy, and `false` otherwise.

Here is an example implementation of the function:

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

You can use the function as follows:

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
