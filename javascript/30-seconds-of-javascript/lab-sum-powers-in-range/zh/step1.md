# 计算给定范围内幂之和的函数

要计算指定范围内（包括两个端点）所有数字的幂之和，请使用以下函数：

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

以下是使用此函数的方法：

- 调用 `sumPower(end)` 来计算从 1 到 `end` 的所有数字的平方和。
- 调用 `sumPower(end, power)` 来计算从 1 到 `end` 的所有数字的 `power` 次幂之和。
- 调用 `sumPower(end, power, start)` 来计算从 `start` 到 `end` 的所有数字的 `power` 次幂之和。

请注意，第二个和第三个参数（`power` 和 `start`）是可选的，如果未提供，则分别默认为 `2` 和 `1`。

示例：

```js
sumPower(10); // 返回 385（1 到 10 的数字的平方和）
sumPower(10, 3); // 返回 3025（1 到 10 的数字的立方和）
sumPower(10, 3, 5); // 返回 2925（5 到 10 的数字的立方和）
```
