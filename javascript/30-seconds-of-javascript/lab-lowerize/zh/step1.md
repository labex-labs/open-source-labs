# 理解 JavaScript 中的对象

在开始将对象的键转换为小写之前，让我们先了解一下什么是 JavaScript 对象，以及如何使用它们。

在 JavaScript 中，对象是键值对的集合。键是字符串（或 Symbol），值可以是任何数据类型，包括其他对象。

让我们从打开 Node.js 交互式 shell 开始：

1. 在你的 WebIDE 中打开终端
2. 输入 `node` 并按回车键

现在你应该会看到 Node.js 提示符 (`>`)，它允许你直接输入 JavaScript 代码。

让我们创建一个带有大小写混合键的简单对象：

```javascript
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};
```

将这段代码输入到 Node.js 提示符中并按回车键。要查看该对象，只需输入 `user` 并按回车键：

```javascript
user;
```

你应该会看到如下输出：

```
{ Name: 'John', AGE: 30, Email: 'john@example.com' }
```

如你所见，这个对象的键具有不同的大小写样式。在下一步中，我们将学习如何访问这些键并将它们转换为小写。
