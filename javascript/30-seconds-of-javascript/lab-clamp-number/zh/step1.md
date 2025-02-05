# 将数字限制在某个范围内的函数

要将一个数字限制在指定范围内，请使用 `clampNumber` 函数。

首先，打开终端/SSH 并输入 `node` 来练习编码。

`clampNumber` 函数接受三个参数：`num`、`a` 和 `b`。它将 `num` 限制在由边界值 `a` 和 `b` 指定的闭区间内，并返回结果。

如果 `num` 在该范围内，函数返回 `num`。否则，它返回该范围内最接近的数字。

以下是 `clampNumber` 函数的代码：

```js
const clampNumber = (num, a, b) =>
  Math.max(Math.min(num, Math.max(a, b)), Math.min(a, b));
```

以下是一些使用该函数的示例：

```js
clampNumber(2, 3, 5); // 3
clampNumber(1, -1, -5); // -1
```
