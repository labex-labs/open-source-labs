# 映射数组的对称差集

要开始编码，请打开终端/SSH 并输入 `node`。

此函数在对两个数组的每个元素应用给定函数之后，返回这两个数组之间的对称差集。其工作原理如下：

- 从每个数组创建一个 `Set`，以便在对它们应用 `fn` 之后获取每个数组的唯一值。
- 对每个 `Set` 使用 `Array.prototype.filter()`，只保留另一个 `Set` 中不包含的值。

以下是 `symmetricDifferenceBy` 函数的代码：

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

你可以这样使用 `symmetricDifferenceBy`：

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
