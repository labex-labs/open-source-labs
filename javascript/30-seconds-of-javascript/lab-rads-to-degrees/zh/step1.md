# 弧度转换为度

要将角度从弧度转换为度，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用以下公式：`degrees = radians * (180 / Math.PI)`
3. 将公式中的 `radians` 替换为你要转换的值。
4. 结果将以度为单位。

以下是一个示例：

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

这将把 `π/2` 弧度转换为 `90` 度。
