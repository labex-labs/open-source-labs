# 创建实用应用程序

既然我们已经有了一个能计算日期差值（以秒为单位）的可用函数，接下来就创建一个更实用的应用程序。我们将构建一个简单的计时器，用于计算从启动计时器开始所经过的时间。

## 创建计时器应用程序

在 WebIDE 中创建一个名为 `timer.js` 的新文件：

1. 点击左侧侧边栏的“Explorer”图标。
2. 在文件资源管理器中右键单击，选择“New File”。
3. 将文件命名为 `timer.js` 并按回车键。
4. 在文件中添加以下代码：

```javascript
// 计算两个日期之间秒数差值的函数
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// 开始时间 - 脚本开始运行的时间
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// 更新并显示已用时间的函数
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // 将时间格式化为 小时：分钟：秒
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // 清空控制台并显示更新后的时间
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// 每秒更新一次计时器
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// 保持脚本运行
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // 运行 1 分钟
```

按 Ctrl+S 或点击“File > Save”保存文件。

## 运行计时器应用程序

要运行计时器应用程序，在终端中使用以下命令：

```bash
node timer.js
```

计时器将启动并每秒更新一次，显示自启动以来经过的时间。计时器将在 1 分钟后自动停止，你也可以通过按 Ctrl+C 提前停止它。

## 理解计时器应用程序

下面来详细分析计时器应用程序的工作原理：

1. 我们定义了 `getSecondsDiffBetweenDates` 函数，用于计算时间差（以秒为单位）。
2. 记录脚本开始运行时的起始时间。
3. 定义 `updateTimer` 函数，该函数：
   - 获取当前时间。
   - 计算自起始时间以来经过的秒数。
   - 将经过的时间格式化为 小时：分钟：秒。
   - 显示格式化后的时间。
4. 使用 `setInterval` 每 1000 毫秒（1 秒）运行一次 `updateTimer` 函数。
5. 使用 `setTimeout` 在 60000 毫秒（1 分钟）后停止计时器。

这个应用程序展示了如何实际运用我们的日期差值函数来创建一个实时计时器。
