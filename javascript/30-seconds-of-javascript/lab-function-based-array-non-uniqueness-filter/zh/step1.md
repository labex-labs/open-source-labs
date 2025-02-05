# 使用函数过滤数组中的非唯一值

要开始练习编码，请打开终端/SSH并输入 `node`。

这段代码根据提供的比较函数从数组中过滤掉非唯一值。实现此目的的步骤如下：

1. 使用 `Array.prototype.filter()` 和 `Array.prototype.every()` 创建一个新数组，该数组仅包含基于比较函数 `fn` 的唯一值。
2. 比较函数接受四个参数：正在比较的两个元素的值及其索引。
3. 函数 `filterNonUniqueBy` 实现上述步骤并返回唯一值数组。

```js
const filterNonUniqueBy = (arr, fn) =>
  arr.filter((v, i) => arr.every((x, j) => (i === j) === fn(v, x, i, j)));
```

以下是如何使用此函数的示例：

```js
filterNonUniqueBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id === b.id
); // [ { id: 2, value: 'c' } ]
```

这段代码简洁、清晰且连贯，应该能按预期工作。
