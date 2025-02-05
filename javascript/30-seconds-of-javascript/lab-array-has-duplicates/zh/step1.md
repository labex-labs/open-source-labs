# 如何检查数组中的重复项

要检查数组中是否有重复值，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Set` 获取数组中的唯一值。
3. 使用 `Set.prototype.size` 和 `Array.prototype.length` 检查唯一值的数量是否与原始数组中的元素数量相同。

以下是一个检查数组中重复项的示例代码片段：

```js
const hasDuplicates = (arr) => new Set(arr).size !== arr.length;
```

你可以使用以下代码测试此函数：

```js
hasDuplicates([0, 1, 1, 2]); // true
hasDuplicates([0, 1, 2, 3]); // false
```

如果数组中有任何重复值，`hasDuplicates` 函数返回 `true`，否则返回 `false`。
