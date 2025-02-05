# How to Find the Longest Item in an Array

To find the longest item in an array, open the Terminal/SSH and type `node`. The function takes any number of iterable objects or objects with a `length` property and returns the longest one. It uses `Array.prototype.reduce()` to compare the length of objects and find the longest one. If multiple objects have the same length, the function returns the first one. If no arguments are provided, it returns `undefined`.

Here is the code:

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

You can use the function like this:

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
