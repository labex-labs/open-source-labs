# 使用各种日期格式进行测试

既然我们已经有了基本的验证函数，那就用不同的日期格式来测试它，以了解它在各种输入下的表现。

## 创建测试套件

让我们创建一个全面的测试套件，来检查不同的日期格式：

1. 创建一个名为 `dateTester.js` 的新文件。
2. 添加以下代码：

```javascript
// Import our isISOString function
const isISOString = require("./isISODate");

// Function to test different date strings
function testDate(description, dateString) {
  console.log(`Testing: ${description}`);
  console.log(`Input: "${dateString}"`);
  console.log(`Is ISO Format: ${isISOString(dateString)}`);
  console.log("-----------------------");
}

// Valid ISO date examples
testDate("Standard ISO date with timezone Z", "2023-05-12T14:30:15.123Z");
testDate("ISO date with zero milliseconds", "2020-10-12T10:10:10.000Z");

// Invalid or non-ISO format examples
testDate("Date only (no time component)", "2023-05-12");
testDate("Date and time without milliseconds", "2023-05-12T14:30:15Z");
testDate(
  "Date with time zone offset instead of Z",
  "2023-05-12T14:30:15+01:00"
);
testDate("Invalid date (month 13 does not exist)", "2023-13-12T14:30:15.123Z");
testDate("Non-date string", "Hello World");
```

3. 在终端中运行测试套件：

```bash
node dateTester.js
```

你应该会看到输出，显示哪些字符串是有效的 ISO 日期，哪些不是。

## 理解测试结果

让我们分析一下每个测试用例有效或无效的原因：

1. `2023-05-12T14:30:15.123Z` —— 这个是有效的，因为它遵循了完整的 ISO 8601 格式，并带有 UTC 时区指示符（Z）。

2. `2020-10-12T10:10:10.000Z` —— 这个也是有效的，其中毫秒数明确设置为 000。

3. `2023-05-12` —— 这是一个有效的日期，但不是 ISO 格式，因为它缺少时间部分。

4. `2023-05-12T14:30:15Z` —— 这看起来像是 ISO 格式，但缺少严格 ISO 格式中必需的毫秒数。

5. `2023-05-12T14:30:15+01:00` —— 这里使用了时区偏移量（+01:00）而不是 'Z'。虽然根据 ISO 8601 这是有效的，但我们的函数要求的是 `toISOString()` 方法生成的精确格式，该格式始终使用 'Z'。

6. `2023-13-12T14:30:15.123Z` —— 这是一个无效的日期（不存在 13 月），因此 `new Date()` 会创建一个无效的日期对象。

7. `Hello World` —— 这根本不是一个日期，所以 `new Date()` 会创建一个无效的日期对象。

我们的验证函数特别检查了两个条件：

1. 字符串必须能解析为有效的日期（不是 NaN）。
2. 当该日期转换回 ISO 字符串时，必须与原始输入完全匹配。

这种方法确保我们验证的是 JavaScript 的 `toISOString()` 方法生成的精确 ISO 格式。
