# 创建一个延迟的 Promise

要创建一个在特定时间后解析的新 Promise，请执行以下步骤：

1. 使用 `Promise` 构造函数创建一个新的 Promise。
2. 在 Promise 的执行器函数内部，使用 `setTimeout()` 在指定的 `delay` 之后使用提供的 `value` 调用 Promise 的 `resolve` 函数。

以下是 `resolveAfter()` 的示例实现：

```js
const resolveAfter = (value, delay) =>
  new Promise((resolve) => {
    setTimeout(() => resolve(value), delay);
  });
```

现在你可以调用 `resolveAfter()` 来获取一个在指定延迟后解析为提供的值的 Promise：

```js
resolveAfter("Hello", 1000);
// 返回一个在 1 秒后解析为 'Hello' 的 Promise
```

要开始练习编码，请打开终端或 SSH 并输入 `node`。
