# 检查一个数字是否为 10 的幂

要检查一个数字是否为 10 的幂，请打开终端/SSH 并输入 `node`。

以下是用于确定 `n` 是否为 10 的幂的代码：

```js
const isPowerOfTen = (n) => Math.log10(n) % 1 === 0;
```

使用 `isPowerOfTen()` 函数来确定给定的数字是否为 10 的幂。

```js
isPowerOfTen(1); // true
isPowerOfTen(10); // true
isPowerOfTen(20); // false
```
