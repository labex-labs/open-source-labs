# 检查一个值是否为布尔值

要检查一个值在 JavaScript 中是否为布尔原始值，请使用 `typeof` 运算符和 `===` 比较运算符。

```js
const isBoolean = (val) => typeof val === "boolean";
```

以下是如何使用 `isBoolean()` 函数检查一个值是否为布尔值的示例：

```js
isBoolean(null); // 返回 false
isBoolean(false); // 返回 true
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
