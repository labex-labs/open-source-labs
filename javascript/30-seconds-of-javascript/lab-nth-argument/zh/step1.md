# 一个获取第 n 个参数的函数

要开始练习编码，请打开终端/SSH 并输入 `node`。以下是如何创建一个获取索引为 `n` 的参数的函数。

- 使用 `Array.prototype.slice()` 来获取索引为 `n` 处的所需参数。
- 如果 `n` 为负数，则返回从末尾开始的第 n 个参数。

```js
const nthArg =
  (n) =>
  (...args) =>
    args.slice(n)[0];
```

以下是如何使用 `nthArg` 函数的示例：

```js
const third = nthArg(2);
console.log(third(1, 2, 3)); // 输出：3
console.log(third(1, 2)); // 输出：undefined

const last = nthArg(-1);
console.log(last(1, 2, 3, 4, 5)); // 输出：5
```
