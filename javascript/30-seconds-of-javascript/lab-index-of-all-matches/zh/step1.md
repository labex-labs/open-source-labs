# 所有匹配项的索引

要在数组中找到 `val` 的所有索引，请使用 `Array.prototype.reduce()` 遍历元素并存储匹配元素的索引。如果 `val` 从未出现过，则返回一个空数组。

```js
const indexOfAll = (arr, val) =>
  arr.reduce((acc, el, i) => (el === val ? [...acc, i] : acc), []);
```

示例用法：

```js
indexOfAll([1, 2, 3, 1, 2, 3], 1); // [0, 3]
indexOfAll([1, 2, 3], 4); // []
```

要开始练习编码，请打开终端/SSH 并输入 `node`。

这是所有匹配项的索引。
