# Checking if All Array Elements Are True

To check if all elements in a collection are `true`, you can use the `Array.prototype.every()` method. This method takes a predicate function as an argument and returns `true` if the function evaluates to `true` for all elements in the array.

To simplify the code, you can use a function called `all` which takes an array and an optional predicate function as arguments. The function uses `Array.prototype.every()` to check if all elements in the array return `true` based on the provided function. If no function is provided, `Boolean` is used as a default.

Here's an example of how to use the `all` function:

```js
const all = (arr, fn = Boolean) => arr.every(fn);

all([4, 2, 3], (x) => x > 1); // true
all([1, 2, 3]); // true
```
