# 如何在 JavaScript 中初始化 N 维数组

要在 JavaScript 中创建 N 维数组，你可以使用 `initializeNDArray` 函数。该函数接受一个值和任意数量的维度作为参数，并返回一个用该值初始化的新数组。

要使用 `initializeNDArray`，你可以按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始编码。
2. 使用递归来创建具有给定维度数量的数组。
3. 使用 `Array.from()` 和 `Array.prototype.map()` 来生成行，其中每一行都是使用 `initializeNDArray()` 初始化的新数组。

以下是 `initializeNDArray` 函数的代码：

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

然后你可以使用所需的值和维度数量调用 `initializeNDArray`。例如：

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
