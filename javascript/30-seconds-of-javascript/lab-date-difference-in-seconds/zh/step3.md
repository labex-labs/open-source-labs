# 使用箭头函数实现日期差值函数

既然我们已经了解了如何计算日期差值，接下来就使用箭头函数实现一个更简洁的日期差值函数。

## JavaScript 中的箭头函数

箭头函数为 JavaScript 中的函数编写提供了更简洁的语法。以下是如何使用箭头函数语法重写我们的日期差值函数：

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

这个函数的功能与我们之前的函数完全相同，但语法更加简洁清晰。

## 创建 JavaScript 文件

我们创建一个 JavaScript 文件来存储和测试这个函数。按 Ctrl+D 或输入 `.exit` 并按回车键，退出 Node.js 环境。

现在，在 WebIDE 中创建一个名为 `dateDifference.js` 的新文件：

1. 点击左侧侧边栏的“Explorer”图标。
2. 在文件资源管理器中右键单击，选择“New File”。
3. 将文件命名为 `dateDifference.js` 并按回车键。
4. 在文件中添加以下代码：

```javascript
// 计算两个日期之间秒数差值的函数
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// 测试示例
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // 预期输出：2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // 预期输出：60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // 预期输出：3600
```

按 Ctrl+S 或点击“File > Save”保存文件。

## 运行 JavaScript 文件

要运行我们刚刚创建的文件，在终端中使用以下命令：

```bash
node dateDifference.js
```

你应该会看到以下输出：

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

这证实了我们的函数运行正常：

- 第一个示例：00:00:15 和 00:00:17 之间的差值是 2 秒。
- 第二个示例：00:00:00 和 00:01:00 之间的差值是 60 秒（1 分钟）。
- 第三个示例：00:00:00 和 01:00:00 之间的差值是 3600 秒（1 小时）。
