# 在特定范围内生成随机整数数组

要在特定范围内生成随机整数数组，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Array.from()` 创建所需长度的空数组。
3. 使用 `Math.random()` 生成随机数并将它们映射到指定范围。使用 `Math.floor()` 将它们转换为整数。
4. 函数 `randomIntArrayInRange()` 接受三个参数：`min`、`max` 和一个可选参数 `n`（默认值为 1）。
5. 使用所需的 `min`、`max` 和 `n` 值调用 `randomIntArrayInRange()` 函数以生成随机整数数组。

以下是代码：

```js
const randomIntArrayInRange = (min, max, n = 1) =>
  Array.from(
    { length: n },
    () => Math.floor(Math.random() * (max - min + 1)) + min
  );
```

示例用法：

```js
randomIntArrayInRange(12, 35, 10); // [ 34, 14, 27, 17, 30, 27, 20, 26, 21, 14 ]
```
