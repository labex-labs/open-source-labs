# 向量角度计算

要计算两个向量之间的夹角（θ），请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Array.prototype.reduce()`、`Math.pow()` 和 `Math.sqrt()` 来计算每个向量的模以及两个向量的点积。
3. 使用 `Math.acos()` 计算反余弦并得到 θ 值。

以下是一个示例代码片段：

```js
const vectorAngle = (x, y) => {
  let mX = Math.sqrt(x.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  let mY = Math.sqrt(y.reduce((acc, n) => acc + Math.pow(n, 2), 0));
  return Math.acos(x.reduce((acc, n, i) => acc + n * y[i], 0) / (mX * mY));
};

vectorAngle([3, 4], [4, 3]); // 0.283794109208328
```

此函数接受两个数组（`x` 和 `y`）作为参数，并返回它们之间的夹角（以弧度为单位）。
