# 二项式系数计算

要计算从 `n` 个物品中无重复且无序地选择 `k` 个物品的方法数，可以使用以下 JavaScript 函数：

```js
const binomialCoefficient = (n, k) => {
  if (Number.isNaN(n) || Number.isNaN(k)) return NaN;
  if (k < 0 || k > n) return 0;
  if (k === 0 || k === n) return 1;
  if (k === 1 || k === n - 1) return n;
  if (n - k < k) k = n - k;
  let res = n;
  for (let j = 2; j <= k; j++) res *= (n - j + 1) / j;
  return Math.round(res);
};
```

要使用该函数，请打开终端/SSH 并输入 `node`。然后，使用所需的值调用该函数。例如：

```js
binomialCoefficient(8, 2); // 28
```

为确保函数正常工作，可以遵循以下步骤：

1. 使用 `Number.isNaN()` 检查两个值中是否有任何一个是 `NaN`。
2. 检查 `k` 是否小于 `0`、大于或等于 `n`、等于 `1` 或 `n - 1`，并返回相应的结果。
3. 检查 `n - k` 是否小于 `k`，并相应地交换它们的值。
4. 从 `2` 循环到 `k`，并计算二项式系数。
5. 使用 `Math.round()` 处理计算中的舍入误差。
