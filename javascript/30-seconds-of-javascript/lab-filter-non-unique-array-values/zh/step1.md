# 如何在 JavaScript 中过滤数组中的非唯一值

要在 JavaScript 中过滤数组中的非唯一值，你可以创建一个只包含唯一值的新数组。方法如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Set` 构造函数和展开运算符（`...`）来创建一个包含原始数组中唯一值的数组。
3. 使用 `Array.prototype.filter()` 创建一个只包含唯一值的数组。

下面是一个实现此功能的示例函数：

```js
const filterNonUnique = (arr) =>
  [...new Set(arr)].filter((i) => arr.indexOf(i) === arr.lastIndexOf(i));
```

你可以将此函数用于任何数组，以过滤掉非唯一值。例如：

```js
filterNonUnique([1, 2, 2, 3, 4, 4, 5]); // [1, 3, 5]
```
