# 如何使用JavaScript筛选数组中的唯一值

要使用JavaScript筛选数组中的唯一值，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Set` 构造函数和展开运算符 (`...`) 来创建一个包含原始数组中唯一值的数组。
3. 使用 `Array.prototype.filter()` 创建一个只包含非唯一值的数组。
4. 定义一个名为 `filterUnique` 的函数，该函数接受一个数组作为参数，并对其应用上述步骤。
5. 使用你的数组作为参数调用 `filterUnique` 函数。

以下是实现此目的的示例代码片段：

```js
const filterUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) !== arr.lastIndexOf(i));

filterUnique([1, 2, 2, 3, 4, 4, 5]); // [2, 4]
```

在上述代码片段中，`filterUnique` 函数接受一个数组，并对其应用 `Set` 构造函数和 `Array.prototype.filter()` 方法，以返回一个只包含非唯一值的数组。
