# 如何使用 JavaScript 找到数组中最后一个匹配元素的索引

要在 JavaScript 数组中找到与特定条件匹配的最后一个元素的索引，请使用 `findLastIndex` 函数。以下是使用方法：

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

`findLastIndex` 函数接受两个参数：要搜索的数组和用于测试每个元素的函数。其工作原理如下：

1. 使用 `Array.prototype.map()` 创建一个新的 `[索引, 值]` 对数组。
2. 使用 `Array.prototype.filter()` 从数组中移除不匹配 `fn` 函数提供的条件的元素。
3. 使用 `Array.prototype.pop()` 获取过滤后数组中的最后一个元素。
4. 如果过滤后的数组为空，则返回 `-1`。

以下是使用 `findLastIndex` 的示例：

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2（值 3 的索引）
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1（未找到时的默认值）
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
