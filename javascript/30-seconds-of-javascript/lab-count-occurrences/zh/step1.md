# 如何在 JavaScript 中统计出现次数

要统计特定值在 JavaScript 数组中出现的次数，可以使用 `Array.prototype.reduce()` 方法。

具体做法如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 复制并粘贴以下代码：

```js
const countOccurrences = (arr, val) =>
  arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
```

3. 在上述代码中，`countOccurrences` 函数接受两个参数：要搜索的数组和要统计的 值。
4. `reduce()` 方法用于遍历数组中的每个元素，并在每次遇到特定值时增加计数器。
5. 要测试该函数，使用数组和值调用它，如下所示：

```js
countOccurrences([1, 1, 2, 1, 2, 3], 1); // 3
```

这将返回 `1` 在数组 `[1, 1, 2, 1, 2, 3]` 中出现的次数，即 `3`。
