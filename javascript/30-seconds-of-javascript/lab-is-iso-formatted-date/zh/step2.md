# 创建一个函数来验证 ISO 格式的日期字符串

在这一步中，我们将创建一个 JavaScript 函数，用于检查给定的字符串是否为有效的 ISO 8601 格式。

## 创建验证函数

让我们为 ISO 日期验证器创建一个新的 JavaScript 文件：

1. 在 WebIDE 中，点击左侧侧边栏的“资源管理器”图标。
2. 在文件资源管理器中右键单击，选择“新建文件”。
3. 将文件命名为 `isISODate.js` 并按回车键。
4. 在文件中添加以下代码：

```javascript
/**
 * Checks if a string is a valid ISO 8601 formatted date string
 * @param {string} val - The string to check
 * @return {boolean} - Returns true if the string is in ISO format, false otherwise
 */
const isISOString = (val) => {
  // Create a Date object from the input string
  const d = new Date(val);

  // Check if the date is valid (not NaN) and if the ISO string matches the original
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

// Export the function so we can use it elsewhere
module.exports = isISOString;
```

让我们来分析一下这个函数的工作原理：

1. `new Date(val)` 从输入字符串创建一个日期对象。
2. `d.valueOf()` 返回数字时间戳值（自 1970 年 1 月 1 日以来的毫秒数）。
3. `Number.isNaN(d.valueOf())` 检查日期是否无效（NaN 表示“非数字”）。
4. `d.toISOString() === val` 验证将日期对象转换回 ISO 字符串是否与原始输入匹配。

## 测试我们的函数

现在，让我们创建一个简单的测试文件来测试我们的函数：

1. 创建另一个名为 `testISO.js` 的文件。
2. 添加以下代码：

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Test with a valid ISO formatted date
console.log("Testing a valid ISO date:");
console.log("2020-10-12T10:10:10.000Z");
console.log("Result:", isISOString("2020-10-12T10:10:10.000Z"));
console.log();

// Test with an invalid format
console.log("Testing a non-ISO date:");
console.log("2020-10-12");
console.log("Result:", isISOString("2020-10-12"));
```

3. 使用 Node.js 运行测试文件：

```bash
node testISO.js
```

你应该会看到类似于以下的输出：

```
Testing a valid ISO date:
2020-10-12T10:10:10.000Z
Result: true

Testing a non-ISO date:
2020-10-12
Result: false
```

这表明我们的函数能够正确识别 "2020-10-12T10:10:10.000Z" 是有效的 ISO 格式日期，而 "2020-10-12" 不是。
