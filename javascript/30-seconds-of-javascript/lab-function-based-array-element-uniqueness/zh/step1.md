# 使用函数检查数组中的所有元素是否唯一

要根据提供的映射函数检查数组中的所有元素是否唯一，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.map()` 方法将提供的函数 `fn` 应用于 `arr` 数组中的所有元素。
3. 从映射值创建一个新的 `Set`，以仅保留唯一出现的值。
4. 使用 `Array.prototype.length` 和 `Set.prototype.size` 方法将唯一映射值的长度与原始数组长度进行比较。

以下是代码：

```js
const allUniqueBy = (arr, fn) => arr.length === new Set(arr.map(fn)).size;
```

你可以使用 `allUniqueBy()` 函数来检查数组中的所有元素是否唯一。例如：

```js
allUniqueBy([1.2, 2.4, 2.9], Math.round); // true
allUniqueBy([1.2, 2.3, 2.4], Math.round); // false
```
