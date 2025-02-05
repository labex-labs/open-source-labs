# 如何用 JavaScript 计算加权平均值

要在 JavaScript 中计算两个或多个数字的加权平均值，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()` 创建值的加权和与权重的总和。
3. 将值的加权和除以权重的总和以获得加权平均值。

以下是 `weightedAverage` 函数的 JavaScript 代码：

```js
const weightedAverage = (nums, weights) => {
  const [sum, weightSum] = weights.reduce(
    (acc, w, i) => {
      acc[0] = acc[0] + nums[i] * w;
      acc[1] = acc[1] + w;
      return acc;
    },
    [0, 0]
  );
  return sum / weightSum;
};
```

你可以使用 `weightedAverage` 函数来计算一组数字和一组权重的加权平均值，如下所示：

```js
weightedAverage([1, 2, 3], [0.6, 0.2, 0.3]); // 1.72727
```
