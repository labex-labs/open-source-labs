# 如何在 JavaScript 中获取函数的名称

要获取 JavaScript 函数的名称，请执行以下步骤：

1. 打开终端或 SSH。
2. 输入 `node` 开始练习编码。
3. 使用 `console.debug()` 和传入函数的 `name` 属性将函数名称记录到控制台的 `debug` 通道。
4. 返回给定函数 `fn`。

以下是一个示例代码片段，展示了如何在 JavaScript 中获取函数的名称：

```js
const functionName = (fn) => (console.debug(fn.name), fn);

let m = functionName(Math.max)(5, 6);
// 函数名称'max' 会记录在控制台的 debug 通道中。
// m = 6
```

在这个示例中，`functionName` 函数将传入函数的名称记录到控制台的 `debug` 通道，并返回函数本身。函数的 `name` 属性用于获取其名称。
