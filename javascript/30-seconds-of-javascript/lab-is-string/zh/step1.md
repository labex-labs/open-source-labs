# 检查一个值是否为字符串

要检查一个值是否为字符串，请使用 `typeof` 关键字，后跟你要检查的值。此方法仅适用于字符串原始类型。

以下是一个检查给定值是否为字符串的示例代码：

```js
const isString = (val) => typeof val === "string";
```

你可以像这样使用 `isString` 函数：

```js
isString("10"); // true
```
