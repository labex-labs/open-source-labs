# 最大子数组算法

要练习编码，请打开终端/SSH 并输入 `node`。此算法用于在一个数字数组中找到具有最大和的连续子数组。要实现此算法，请按照以下步骤操作：

- 使用贪心算法来跟踪当前的 `sum` 和当前的最大值 `maxSum`。将 `maxSum` 设置为 `-Infinity`，以确保如果所有值都是负数，则返回最高的负值。
- 定义变量来跟踪最大起始索引 `sMax`、最大结束索引 `eMax` 和当前起始索引 `s`。
- 使用 `Array.prototype.forEach()` 遍历数组中的值，并将当前值加到 `sum` 中。
- 如果当前的 `sum` 大于 `maxSum`，则更新索引值和 `maxSum`。
- 如果 `sum` 小于 `0`，则将其重置为 `0`，并将 `s` 的值更新为下一个索引。
- 使用 `Array.prototype.slice()` 返回由索引变量指示的子数组。

以下是该算法的 JavaScript 代码：

```js
const maxSubarray = (...arr) => {
  let maxSum = -Infinity,
    sum = 0;
  let sMax = 0,
    eMax = arr.length - 1,
    s = 0;

  arr.forEach((n, i) => {
    sum += n;
    if (maxSum < sum) {
      maxSum = sum;
      sMax = s;
      eMax = i;
    }

    if (sum < 0) {
      sum = 0;
      s = i + 1;
    }
  });

  return arr.slice(sMax, eMax + 1);
};
```

以下是使用该函数的示例：

```js
maxSubarray(-2, 1, -3, 4, -1, 2, 1, -5, 4); // [4, -1, 2, 1]
```
