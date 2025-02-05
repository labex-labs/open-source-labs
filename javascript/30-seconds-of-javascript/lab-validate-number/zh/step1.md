# 数字验证函数

要验证给定输入是否为数字，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `parseFloat()` 尝试将输入转换为数字。
- 使用 `Number.isNaN()` 和逻辑非 (`!`) 运算符检查输入是否为数字。
- 使用 `Number.isFinite()` 检查输入是否为有限数。
- 使用 `Number` 和宽松相等运算符 (`==`) 检查强制类型转换是否成立。

以下是 `validateNumber` 函数的代码：

```js
const validateNumber = (input) => {
  const num = parseFloat(input);
  return !Number.isNaN(num) && Number.isFinite(num) && Number(input) == input;
};
```

你可以按如下方式使用 `validateNumber` 函数：

```js
validateNumber("10"); // true
validateNumber("a"); // false
```
