# 理解 JavaScript 字符串表示法

在计算字符串的字节大小之前，了解字符串在 JavaScript 中的表示方式非常重要。

在 JavaScript 中，字符串是 UTF-16 代码单元的序列。这意味着像表情符号或某些符号这样的字符可能需要多个字节来表示。例如，一个简单的英文字母占 1 个字节，但一个表情符号可能占 4 个字节。

让我们从在终端中启动 Node.js 开始：

1. 点击 WebIDE 界面中的终端图标打开终端。
2. 输入以下命令并按回车键：

```bash
node
```

你现在应该进入了 Node.js 交互式控制台，它看起来大概是这样的：

```
Welcome to Node.js v14.x.x.
Type ".help" for more information.
>
```

![Open the node](../assets/screenshot-20250306-cFJ9GgLX@2x.png)

在这个控制台中，你可以直接试验 JavaScript 代码。尝试输入以下命令来查看字符串的长度：

```javascript
"Hello World".length;
```

你应该会看到输出：

```
11
```

这给出了字符数量，但不是实际的字节大小。字符数量和字节大小可能不同，尤其是在包含特殊字符的情况下。让我们在下一步中进一步探讨这个问题。
