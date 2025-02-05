# 如何检查数组中的所有元素是否唯一

要检查数组中的所有元素是否唯一，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 根据映射值创建一个新的 `Set`，以仅保留唯一出现的元素。
3. 使用 `Array.prototype.length` 和 `Set.prototype.size` 来比较唯一值的长度与原始数组的长度。

以下是一个实现这些步骤的示例函数：

```js
const allUnique = (arr) => arr.length === new Set(arr).size;
```

你可以使用此函数来检查数组是否具有所有唯一元素，如下所示：

```js
allUnique([1, 2, 3, 4]); // true
allUnique([1, 1, 2, 3]); // false
```
