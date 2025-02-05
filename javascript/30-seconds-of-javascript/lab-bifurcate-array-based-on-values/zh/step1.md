# 将数组拆分为两个组的函数

要使用此函数根据值将数组拆分为两个组，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `bifurcate()` 函数，它根据给定的 `filter` 数组的结果将值拆分为两个组。
3. 要实现该函数，请使用 `Array.prototype.reduce()` 和 `Array.prototype.push()` 根据 `filter` 数组将元素添加到组中。
4. 如果 `filter` 对任何元素具有真值，则将其添加到第一组；否则，将其添加到第二组。

以下是 `bifurcate()` 函数的代码：

```js
const bifurcate = (arr, filter) =>
  arr.reduce(
    (acc, val, i) => (acc[filter[i] ? 0 : 1].push(val), acc),
    [[], []]
  );
```

你可以使用值数组和相应的筛选器数组调用 `bifurcate()` 函数，以将值拆分为两个组。例如：

```js
bifurcate(["beep", "boop", "foo", "bar"], [true, true, false, true]);
// [ ['beep', 'boop', 'bar'], ['foo'] ]
```
