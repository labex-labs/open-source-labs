# 在 JavaScript 中初始化映射数组

要在 JavaScript 中初始化映射数组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array()` 构造函数创建所需长度的数组。
3. 使用 `Array.prototype.fill()` 用 `null` 值填充数组。
4. 使用 `Array.prototype.map()`，通过提供的函数 `mapFn` 用所需值填充数组。
5. 省略第二个参数 `mapFn`，将每个元素映射到其索引。

以下是一个示例代码片段：

```js
const initializeMappedArray = (n, mapFn = (_, i) => i) =>
  Array(n).fill(null).map(mapFn);
```

你可以使用 `initializeMappedArray` 函数创建具有所需值的映射数组：

```js
initializeMappedArray(5); // [0, 1, 2, 3, 4]
initializeMappedArray(5, (i) => `item ${i + 1}`);
// ['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
```
