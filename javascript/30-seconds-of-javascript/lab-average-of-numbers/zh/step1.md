# 如何在 JavaScript 中计算数字的平均值

要在 JavaScript 中计算两个或多个数字的平均值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用内置的 `Array.prototype.reduce()` 方法将每个值添加到初始值为 `0` 的累加器中。
3. 将得到的总和除以数组的长度。

以下是一个你可以使用的示例代码片段：

```js
const average = (...nums) =>
  nums.reduce((acc, val) => acc + val, 0) / nums.length;
```

你可以使用数组或多个参数调用 `average` 函数：

```js
average(...[1, 2, 3]); // 2
average(1, 2, 3); // 2
```
