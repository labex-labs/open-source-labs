# 扁平迭代器解释

要创建一个遍历可迭代对象并展平嵌套可迭代对象的生成器，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 在生成器函数中使用递归。
3. 使用 `for...of` 循环遍历给定可迭代对象的值。
4. 使用 `Symbol.iterator` 检查每个值是否为可迭代对象。
5. 如果是，则使用 `yield*` 表达式递归委托给同一个生成器函数。
6. 否则，`yield` 当前值。

以下是一个示例代码片段：

```js
const flatIterator = function* (itr) {
  for (let item of itr) {
    if (item[Symbol.iterator]) yield* flatIterator(item);
    else yield item;
  }
};

const arr = [1, 2, [3, 4], [5, [6, [7], 8]], 9, new Set([10, 11])];
[...flatIterator(arr)]; // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
```

在示例中，`arr` 是一个值数组，包括嵌套数组和一个集合。`flatIterator` 生成器函数用于展平这些嵌套值并返回一个展平后的数组。
