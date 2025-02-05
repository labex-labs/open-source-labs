# 如何使用 JavaScript 在数组的特定索引处插入值

要使用 JavaScript 在数组的特定索引处插入值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.splice()` 方法，传入适当的索引和删除计数 `0`，展开要插入的给定值。
3. `insertAt` 函数接受一个数组、一个索引以及一个或多个要在指定索引之后插入的值。
4. 该函数会改变原始数组并返回修改后的数组。

以下是 `insertAt` 函数的实际应用示例：

```js
const insertAt = (arr, i, ...v) => {
  arr.splice(i + 1, 0, ...v);
  return arr;
};

let myArray = [1, 2, 3, 4];
insertAt(myArray, 2, 5); // myArray = [1, 2, 3, 5, 4]

let otherArray = [2, 10];
insertAt(otherArray, 0, 4, 6, 8); // otherArray = [2, 4, 6, 8, 10]
```

在上述示例中，`insertAt` 函数用于在 `myArray` 数组的第二个索引之后插入值 `5`，并在 `otherArray` 数组的第一个索引之后插入值 `4`、`6` 和 `8`。
