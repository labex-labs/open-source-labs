# 标准差

要在 JavaScript 中计算一组数字的标准差，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用下面提供的函数 `standardDeviation(arr, usePopulation = false)`。
3. 将一组数字作为第一个参数传递给该函数。
4. 省略第二个参数 `usePopulation` 以获得样本标准差。将其设置为 `true` 以获得总体标准差。

```js
const standardDeviation = (arr, usePopulation = false) => {
  const mean = arr.reduce((acc, val) => acc + val, 0) / arr.length;
  return Math.sqrt(
    arr
      .reduce((acc, val) => acc.concat((val - mean) ** 2), [])
      .reduce((acc, val) => acc + val, 0) /
      (arr.length - (usePopulation ? 0 : 1))
  );
};
```

示例用法：

```js
standardDeviation([10, 2, 38, 23, 38, 23, 21]); // 13.284434142114991（样本）
standardDeviation([10, 2, 38, 23, 38, 23, 21], true); // 12.29899614287479（总体）
```
