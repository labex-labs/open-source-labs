# JavaScript Date 对象入门

JavaScript 提供了一个内置的 `Date` 对象，让我们可以处理日期和时间。在计算日期之间的差值之前，我们先来了解如何在 JavaScript 中创建和使用 `Date` 对象。

## 启动 Node.js 环境

我们先打开交互式的 Node.js 环境：

1. 点击 WebIDE 顶部的“Terminal”菜单，打开终端。
2. 输入以下命令并按回车键：

```bash
node
```

你现在应该能看到 Node.js 提示符 (`>`)，这表明你已进入 JavaScript 交互式环境。这样你就可以直接在终端中执行 JavaScript 代码。

![node-prompt](../assets/screenshot-20250306-328ScUbO@2x.png)

## 创建 Date 对象

在 JavaScript 中，我们可以通过多种方式创建新的 `Date` 对象：

```javascript
// 当前日期和时间
let now = new Date();
console.log(now);

// 特定的日期和时间（年、月 [0-11]、日、时、分、秒）
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // 2023 年 1 月 15 日，10:30:45
console.log(specificDate);

// 从字符串创建日期
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

在 Node.js 环境中输入这些示例代码，并观察输出结果。

请注意，在 JavaScript 中，月份是从 0 开始索引的，即 0 表示 1 月，1 表示 2 月，依此类推。

## 从 Date 对象获取时间戳

JavaScript 中的每个 `Date` 对象内部都将时间存储为自 1970 年 1 月 1 日（UTC）以来经过的毫秒数，这被称为时间戳（timestamp）。

```javascript
let now = new Date();
console.log(now.getTime()); // 获取以毫秒为单位的时间戳
```

这个时间戳对于计算日期之间的差值很有用。
