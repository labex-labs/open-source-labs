# 如何在 JavaScript 中过滤出匹配的数组元素

要在 JavaScript 数组中过滤出具有一个或多个指定值的元素，请执行以下步骤：

1. 打开终端或 SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.includes()` 方法查找要排除的值。
3. 使用 `Array.prototype.filter()` 方法创建一个排除这些元素的新数组。

以下是一个示例代码片段：

```js
const without = (arr, ...args) => arr.filter((v) => !args.includes(v));

without([2, 1, 2, 3], 1, 2); // [3]
```

在这个示例中，`without` 函数接受一个数组 `arr` 和一个或多个参数 `args`。该函数使用 `filter()` 方法创建一个新数组，该数组排除了与 `args` 中任何指定值匹配的任何元素。`includes()` 方法用于检查该值是否在 `args` 中。最后，函数返回包含排除元素的新数组。
