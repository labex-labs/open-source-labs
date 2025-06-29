# 理解问题并进行设置

在开始编码之前，让我们先明确 `replaceLast` 函数应该实现的功能：

1. 接受三个参数：
   - `str`：需要修改的输入字符串
   - `pattern`：要搜索的子字符串或正则表达式
   - `replacement`：用于替换最后一次出现内容的字符串

2. 返回一个新字符串，其中模式的最后一次出现已被替换。

让我们创建一个 JavaScript 文件来实现这个函数：

1. 在 WebIDE 文件资源管理器中导航到项目目录。
2. 在 `replace-last` 目录下创建一个名为 `replaceLast.js` 的新文件。
3. 在文件中添加以下基本结构：

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

为了检查一切是否设置正确，让我们添加一个简单的测试：

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

现在，让我们运行代码，看看当前的输出：

1. 在 WebIDE 中打开终端。
2. 导航到 `replace-last` 目录：
   ```bash
   cd ~/project/replace-last
   ```
3. 使用 Node.js 运行 JavaScript 文件：
   ```bash
   node replaceLast.js
   ```

你应该会在输出中看到 `Hello world world`，因为我们的函数目前只是返回原始字符串，没有做任何修改。
