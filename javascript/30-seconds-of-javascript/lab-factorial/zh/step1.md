# 计算一个数的阶乘

要计算一个数的阶乘，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用递归计算阶乘。
3. 如果 `n` 小于或等于 `1`，则返回 `1`。
4. 否则，返回 `n` 与 `n - 1` 的阶乘的乘积。
5. 如果 `n` 是负数，则抛出 `TypeError`。

以下是计算阶乘的代码：

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

你可以通过将一个数字作为参数调用 `factorial` 函数来测试代码：

```js
factorial(6); // 720
```
