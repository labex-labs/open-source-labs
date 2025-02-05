# 向量距离计算

要计算两个向量之间的距离，请遵循以下步骤：

1. 打开终端/SSH 开始练习编码。
2. 输入 `node` 开始。
3. 使用 `Array.prototype.reduce()`、`Math.pow()` 和 `Math.sqrt()` 来找到向量之间的欧几里得距离。
4. 应用如下所示的 `vectorDistance` 公式：

```js
const vectorDistance = (x, y) =>
  Math.sqrt(x.reduce((acc, val, i) => acc + Math.pow(val - y[i], 2), 0));
```

5. 通过以下格式输入两个向量来测试该公式：`vectorDistance([10, 0, 5], [20, 0, 10]);`
6. 输出将是两个向量之间的距离：`11.180339887498949`。
