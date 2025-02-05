# 数组唯一对称差函数

为了练习编码，打开终端/SSH 并输入 `node`。以下函数返回两个数组之间的唯一对称差。它会从任一数组中移除重复值。

要实现这一点，对每个数组使用 `Array.prototype.filter()` 和 `Array.prototype.includes()` 来移除另一个数组中包含的值。根据结果创建一个 `Set` 以移除重复值。

```js
const uniqueSymmetricDifference = (a, b) => [
  ...new Set([
    ...a.filter((v) => !b.includes(v)),
    ...b.filter((v) => !a.includes(v))
  ])
];
```

按如下方式使用该函数：

```js
uniqueSymmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
uniqueSymmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 3]
```
