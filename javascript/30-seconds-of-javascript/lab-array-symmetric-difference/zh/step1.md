# 数组的对称差集

要找到两个数组之间的对称差集并包含重复值，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 从每个数组创建一个 `Set` 以获取每个数组的唯一值。
3. 对它们各自使用 `Array.prototype.filter()` 仅保留另一个数组中不包含的值。

以下是代码：

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

你可以使用以下示例来测试该函数：

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
