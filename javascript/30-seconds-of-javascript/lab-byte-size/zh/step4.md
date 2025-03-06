# 创建一个实用示例文件

现在，让我们创建一个 JavaScript 文件，以更实用的方式实现我们的字节大小计算函数。这将展示你如何在实际应用中使用这个函数。

1. 在 WebIDE 中创建一个新文件。点击文件资源管理器侧边栏中的 “New File” 图标，并将其命名为 `byteSizeCalculator.js`。

2. 在文件中添加以下代码：

```javascript
/**
 * Calculate the byte size of a given string.
 * @param {string} str - The string to calculate the byte size for.
 * @returns {number} The size in bytes.
 */
function calculateByteSize(str) {
  return new Blob([str]).size;
}

// Examples with different types of strings
const examples = [
  "Hello World",
  "😀",
  "The quick brown fox jumps over the lazy dog",
  "123!@#$%^&*()",
  "Hello, 世界!",
  "😀😃😄😁"
];

// Display the results
console.log("String Byte Size Calculator\n");
console.log("String".padEnd(45) + "| Characters | Bytes");
console.log("-".repeat(70));

examples.forEach((example) => {
  console.log(
    `"${example}"`.padEnd(45) +
      `| ${example.length}`.padEnd(12) +
      `| ${calculateByteSize(example)}`
  );
});
```

3. 按下 Ctrl+S 或从菜单中选择 “File > Save” 来保存文件。

4. 从终端运行该文件：

```bash
node byteSizeCalculator.js
```

你应该会看到类似于以下的输出：

```
String Byte Size Calculator

String                                      | Characters | Bytes
----------------------------------------------------------------------
"Hello World"                               | 11         | 11
"😀"                                        | 1          | 4
"The quick brown fox jumps over the lazy dog" | 43         | 43
"123!@#$%^&*()"                            | 13         | 13
"Hello, 世界!"                              | 10         | 13
"😀😃😄😁"                                  | 4          | 16
```

这个表格清晰地展示了不同类型字符串的字符数量和字节大小之间的差异。

在以下情况下，理解这些差异至关重要：

- 设置网页表单中用户输入的限制
- 计算文本数据的存储需求
- 处理有大小限制的 API
- 优化网络数据传输
