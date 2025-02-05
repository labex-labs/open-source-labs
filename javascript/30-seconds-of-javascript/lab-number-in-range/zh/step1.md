# 检查数字是否在给定范围内的函数

要检查一个数字是否落在指定范围内，请使用 `inRange` 函数。首先打开终端/SSH，输入 `node` 开始编码。

以下是使用 `inRange` 函数的步骤：

1. 使用算术比较来检查给定数字是否在指定范围内。
2. 如果第二个参数 `end` 未指定，则范围被视为从 `0` 到 `start`。
3. `inRange` 函数接受三个参数：`n`、`start` 和 `end`。
4. 如果 `end` 小于 `start`，函数会交换 `start` 和 `end` 的值。
5. 如果 `end` 未指定，函数会检查 `n` 是否大于或等于 `0` 且小于 `start`。
6. 如果 `end` 已指定，函数会检查 `n` 是否大于或等于 `start` 且小于 `end`。
7. 如果 `n` 在指定范围内，函数返回 `true`，否则返回 `false`。

以下是 `inRange` 函数：

```js
const inRange = (n, start, end = null) => {
  if (end && start > end) [end, start] = [start, end];
  return end == null ? n >= 0 && n < start : n >= start && n < end;
};
```

以下是一些使用 `inRange` 函数的示例：

```js
inRange(3, 2, 5); // true
inRange(3, 4); // true
inRange(2, 3, 5); // false
inRange(3, 2); // false
```
