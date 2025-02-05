# 如何在 JavaScript 中获取数组的最后 N 个元素

要在 JavaScript 中获取数组的最后 `n` 个元素，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。

2. 使用 `Array.prototype.slice()` 并将起始值设为 `-n`，以获取数组的最后 `n` 个元素。

以下是获取数组最后 `n` 个元素的 JavaScript 代码：

```js
const lastN = (arr, n) => arr.slice(-n);
```

要测试此代码，请使用数组和你想要获取的元素数量调用 `lastN()` 函数，如下所示：

```js
lastN(["a", "b", "c", "d"], 2); // ['c', 'd']
```
