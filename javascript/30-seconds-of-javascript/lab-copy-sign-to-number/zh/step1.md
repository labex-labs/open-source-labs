# 将一个数字的符号复制到另一个数字的函数

要开始练习编码，请打开终端/SSH 并输入 `node`。

`copySign` 函数返回第一个数字的绝对值，但带有第二个数字的符号。要实现这一点：

1. 使用 `Math.sign()` 检查两个数字是否具有相同的符号。
2. 如果是，则返回 `x`，否则返回 `-x`。

以下是 `copySign` 函数的代码：

```js
const copySign = (x, y) => (Math.sign(x) === Math.sign(y) ? x : -x);
```

你可以使用以下代码测试该函数：

```js
copySign(2, 3); // 2
copySign(2, -3); // -2
copySign(-2, 3); // 2
copySign(-2, -3); // -2
```
