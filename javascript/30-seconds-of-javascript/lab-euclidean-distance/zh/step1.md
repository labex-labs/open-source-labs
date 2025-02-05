# 欧几里得距离计算

要计算任意维度下两点之间的距离，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Object.keys()` 和 `Array.prototype.map()` 将每个坐标映射为两点之间的差值。
3. 使用 `Math.hypot()` 计算两点之间的欧几里得距离。

以下是一个示例代码片段，帮助你入门：

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

你可以使用以下示例输入来测试该函数：

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
