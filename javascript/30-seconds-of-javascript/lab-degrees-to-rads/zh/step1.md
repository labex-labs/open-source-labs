# 将角度从度转换为弧度

要将角度从度转换为弧度，请遵循以下步骤：

1. 打开终端/SSH。
2. 输入 `node` 开始编码。
3. 使用度到弧度的公式以及 `Math.PI`。
4. 将公式应用于角度（以度为单位），以得到弧度表示的角度。

以下是JavaScript中的公式：

```js
const degreesToRads = (deg) => (deg * Math.PI) / 180.0;
```

例如，如果你想将90度转换为弧度，可以像这样使用 `degreesToRads` 函数：

```js
degreesToRads(90.0); // ~1.5708
```
