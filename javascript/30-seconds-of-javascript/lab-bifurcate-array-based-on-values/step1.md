# Function to Split Array into Two Groups

To use this function to split an array into two groups based on the values, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `bifurcate()` function, which splits values into two groups based on the result of the given `filter` array.
3. To implement the function, use `Array.prototype.reduce()` and `Array.prototype.push()` to add elements to groups, based on the `filter` array.
4. If `filter` has a truthy value for any element, add it to the first group; otherwise, add it to the second group.

Here is the code for the `bifurcate()` function:

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []],
  );
```

You can call the `bifurcate()` function with an array of values and a corresponding filter array to split the values into two groups. For example:

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
