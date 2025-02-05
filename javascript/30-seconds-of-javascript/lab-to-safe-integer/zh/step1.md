# 将值转换为安全整数

要将一个值转换为安全整数，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `Math.max()` 和 `Math.min()` 找到最接近的安全值。
3. 使用 `Math.round()` 将该值转换为整数。

以下是一个示例代码片段，展示了如何将一个值转换为安全整数：

```js
const toSafeInteger = (num) =>
  Math.round(
    Math.max(Math.min(num, Number.MAX_SAFE_INTEGER), Number.MIN_SAFE_INTEGER)
  );
```

你可以使用以下输入测试此函数：

```js
toSafeInteger("3.2"); // 3
toSafeInteger(Infinity); // 9007199254740991
```
