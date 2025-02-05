# 检查一个值是否为函数

要检查一个值是否为函数，可以使用 `typeof` 运算符和 `function` 原始值。

下面是一个检查给定值是否为函数的函数示例：

```js
const isFunction = (val) => typeof val === "function";
```

你可以这样使用它：

```js
isFunction("x"); // false
isFunction((x) => x); // true
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
