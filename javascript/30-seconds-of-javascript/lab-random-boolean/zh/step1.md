# 如何在 JavaScript 中生成随机布尔值

要在 JavaScript 中生成随机布尔值，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`Math.random()`方法生成一个随机数。
3. 检查随机数是否大于或等于`0.5`。
4. 如果数字大于或等于`0.5`，则返回`true`，否则返回`false`。

以下是该代码的简洁实现：

```js
const randomBoolean = () => Math.random() >= 0.5;
```

你可以通过调用`randomBoolean()`来测试该函数，它将返回`true`或`false`。
