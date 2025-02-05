# 检查一个值是否为 JavaScript 中的异步函数

要检查一个值在 JavaScript 中是否为 `async` 函数，可以使用以下代码：

```js
const isAsyncFunction = (val) =>
  Object.prototype.toString.call(val) === "[object AsyncFunction]";
```

此函数使用 `Object.prototype.toString()` 和 `Function.prototype.call()` 来检查给定参数是否为 `async` 函数。

你可以通过将一个常规函数和一个 `async` 函数作为参数传递来测试该函数：

```js
isAsyncFunction(function () {}); // false
isAsyncFunction(async function () {}); // true
```

要开始练习 JavaScript 编码，请打开终端/SSH 并输入 `node`。
