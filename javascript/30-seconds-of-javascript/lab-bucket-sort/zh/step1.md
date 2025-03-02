# 桶排序算法

要使用桶排序算法对数字数组进行排序，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Math.min()`、`Math.max()` 和展开运算符 (`...`) 找到给定数组的最小值和最大值。
3. 使用 `Array.from()` 和 `Math.floor()` 创建适当数量的 `桶`（空数组）。
4. 使用 `Array.prototype.forEach()` 用数组中的适当元素填充每个桶。
5. 对每个桶进行排序，并使用 `Array.prototype.reduce()`、展开运算符 (`...`) 和 `Array.prototype.sort()` 将其追加到结果中。

以下是 JavaScript 中桶排序算法的一个示例实现：

```js
const bucketSort = (arr, size = 5) => {
  const min = Math.min(...arr);
  const max = Math.max(...arr);
  const buckets = Array.from(
    { length: Math.floor((max - min) / size) + 1 },
    () => []
  );
  arr.forEach((val) => {
    buckets[Math.floor((val - min) / size)].push(val);
  });
  return buckets.reduce((acc, b) => [...acc, ...b.sort((a, b) => a - b)], []);
};
```

要测试该算法，请运行以下代码：

```js
bucketSort([6, 3, 4, 1]); // [1, 3, 4, 6]
```
