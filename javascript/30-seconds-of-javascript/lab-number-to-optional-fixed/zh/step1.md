# 将数字转换为定点表示法

要将数字转换为无尾随零的定点表示法，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Number.prototype.toFixed()` 将数字转换为定点表示法字符串。
3. 使用 `Number.parseFloat()` 将定点表示法字符串转换回数字，去除尾随零。
4. 使用模板字面量将数字转换为字符串。

示例代码：

```js
const toOptionalFixed = (num, digits) =>
  `${Number.parseFloat(num.toFixed(digits))}`;
```

你可以使用不同的输入测试该函数：

```js
toOptionalFixed(1, 2); // '1'
toOptionalFixed(1.001, 2); // '1'
toOptionalFixed(1.5, 2); // '1.5'
```
