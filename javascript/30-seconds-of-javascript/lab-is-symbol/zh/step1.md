# 检查 JavaScript 中的值是否为符号

要检查一个值在 JavaScript 中是否为符号原始类型，你可以使用 `typeof` 运算符。下面是一个你可以使用的示例代码片段：

```js
const isSymbol = (val) => typeof val === "symbol";
```

你可以调用 `isSymbol` 函数并传入一个符号作为参数，以检查它是否返回 `true`。下面是一个示例：

```js
isSymbol(Symbol("x")); // true
```
