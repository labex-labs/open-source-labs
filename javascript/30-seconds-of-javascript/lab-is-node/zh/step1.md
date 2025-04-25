# 如何确定当前运行时环境是否为 Node.js

要确定当前运行时环境是否为 Node.js，请执行以下步骤：

1. 打开终端/SSH。
2. 输入`node`。
3. 使用提供有关当前 Node.js 进程信息的`process`全局对象。
4. 检查`process`、`process.versions`和`process.versions.node`是否已定义。

以下是用于确定当前运行时环境是否为 Node.js 的代码：

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

你可以通过调用`isNode`函数来测试这段代码：

```js
isNode(); // true（Node）
isNode(); // false（浏览器）
```
