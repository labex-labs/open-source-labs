# 将数组拆分为两组的函数

要根据给定函数的结果将数组拆分为两组，请执行以下步骤：

1. 打开终端/SSH并输入 `node` 以开始练习编码。
2. 使用 `Array.prototype.reduce()` 和 `Array.prototype.push()` 方法将元素添加到组中。这是基于给定函数 `fn` 对每个元素返回的值。
3. 如果 `fn` 对任何元素返回真值，则将其添加到第一组。否则，将其添加到第二组。

以下是代码：

```js
const bifurcateBy = (arr, fn) =>
  arr.reduce(
    (acc, val, i) => (acc[fn(val, i) ? 0 : 1].push(val), acc),
    [[], []]
  );
```

例如，如果你调用 `bifurcateBy(['beep', 'boop', 'foo', 'bar'], x => x[0] === 'b')`，该函数将返回 `[ ['beep', 'boop', 'bar'], ['foo'] ]`。
