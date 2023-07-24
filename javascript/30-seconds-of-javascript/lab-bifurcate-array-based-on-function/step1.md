# Function to Split an Array into Two Groups

To split an array into two groups based on the result of a given function, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `Array.prototype.reduce()` and `Array.prototype.push()` methods to add elements to groups. This is based on the value returned by the given function `fn` for each element.
3. If `fn` returns a truthy value for any element, add it to the first group. Otherwise, add it to the second group.

Here's the code:

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

For example, if you call `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')`, the function will return `[ ['beep', 'boop', 'bar'], ['foo'] ]`.
