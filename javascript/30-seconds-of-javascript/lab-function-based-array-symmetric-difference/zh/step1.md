# 用于查找数组对称差集的函数

要使用提供的函数作为比较器来查找两个数组之间的对称差集，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.filter()` 和 `Array.prototype.findIndex()` 方法来找到合适的值。
3. 使用给定的代码执行操作。

```js
const symmetricDifferenceWith = (arr, val, comp) => [
  ...arr.filter((a) => val.findIndex((b) => comp(a, b)) === -1),
  ...val.filter((a) => arr.findIndex((b) => comp(a, b)) === -1)
];
```

例如，考虑以下输入：

```js
symmetricDifferenceWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
); // [1, 1.2, 3.9]
```

上述代码将返回 `[1, 1.2, 3.9]` 作为两个数组之间的对称差集。
