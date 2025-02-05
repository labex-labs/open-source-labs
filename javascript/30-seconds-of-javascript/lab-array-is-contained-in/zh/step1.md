# 检查一个数组是否包含在另一个数组中的函数

要开始编码，请打开终端/SSH并输入 `node`。此函数检查第一个数组的所有元素是否都存在于第二个数组中，而不管它们的顺序如何。

以下是具体步骤：

1. 使用 `for...of` 循环遍历从第一个数组创建的 `Set`。
2. 应用 `Array.prototype.some()` 来验证第二个数组中是否存在所有不同的值。
3. 使用 `Array.prototype.filter()` 来比较两个数组中每个不同值的出现次数。
4. 如果第一个数组中任何元素的计数大于第二个数组中的计数，则返回 `false`。否则，返回 `true`。

查看以下代码以了解其工作原理：

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

要测试该函数，请使用以下代码：

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
