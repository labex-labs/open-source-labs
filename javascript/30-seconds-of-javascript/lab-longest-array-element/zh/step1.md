# 如何找到数组中最长的元素

要找到数组中最长的元素，请打开终端/SSH 并输入 `node`。该函数接受任意数量的可迭代对象或具有 `length` 属性的对象，并返回最长的那个。它使用 `Array.prototype.reduce()` 来比较对象的长度并找到最长的那个。如果多个对象具有相同的长度，该函数返回第一个。如果没有提供参数，则返回 `undefined`。

以下是代码：

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

你可以这样使用该函数：

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
