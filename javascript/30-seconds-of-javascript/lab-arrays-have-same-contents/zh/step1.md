# 检查数组中的相同内容

要检查两个数组是否包含相同的元素（无论顺序如何），请执行以下步骤：

1. 打开终端/SSH并输入 `node`。
2. 对从两个数组的值创建的 `Set` 使用 `for...of` 循环。
3. 使用 `Array.prototype.filter()` 来比较两个数组中每个不同值的出现次数。
4. 如果任何元素的计数不匹配，则返回 `false`，否则返回 `true`。

以下是实现此功能的代码：

```js
const haveSameContents = (a, b) => {
  for (const v of new Set([...a, ...b]))
    if (a.filter((e) => e === v).length !== b.filter((e) => e === v).length)
      return false;
  return true;
};
```

要测试该函数，请使用以下代码：

```js
haveSameContents([1, 2, 4], [2, 4, 1]); // true
```
