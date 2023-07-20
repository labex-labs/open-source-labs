# How to Find the First N Matches

To find the first `n` elements that meet a certain criteria, use the `findFirstN` function. Here's how:

1. Open the Terminal/SSH.
2. Type `node` to start practicing coding.
3. Use the `findFirstN` function, passing in the array to search through, a matching function, and the number of matches to find (if not specified, the default is 1).
4. The `matcher` function will be executed for each element of the `arr`, and if it returns a truthy value, that element will be added to the results array.
5. If the `res` array reaches a length of `n`, the function will return the results array.
6. If no matches are found, an empty array will be returned.

Here's the code for the `findFirstN` function:

```js
const findFirstN = (arr, matcher, n = 1) => {
  let res = [];
  for (let i in arr) {
    const el = arr[i];
    const match = matcher(el, i, arr);
    if (match) res.push(el);
    if (res.length === n) return res;
  }
  return res;
};
```

And here are some examples of how to use it:

```js
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 2); // [2, 4]
findFirstN([1, 2, 4, 6], (n) => n % 2 === 0, 5); // [2, 4, 6]
```
