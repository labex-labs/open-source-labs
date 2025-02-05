# 如何在 JavaScript 中找出数组的相似度

为了练习编码，打开终端/SSH 并输入 `node`。这将帮助你理解如何找出同时出现在两个数组中的元素数组。请按照以下步骤操作：

1. 使用 `Array.prototype.includes()` 方法来确定哪些值不属于 `values`。
2. 使用 `Array.prototype.filter()` 方法将它们移除。

以下是找出数组相似度的代码：

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

你可以通过运行以下命令来测试这段代码：

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

这将返回 `[1, 2]` 作为输出。
