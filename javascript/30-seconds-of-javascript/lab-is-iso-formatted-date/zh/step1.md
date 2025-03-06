# 理解 ISO 日期格式和 JavaScript 日期对象

在开始编码之前，让我们先了解一下 ISO 8601 日期格式是什么，以及 JavaScript 如何处理日期。

## ISO 8601 日期格式

ISO 8601 格式是一种表示日期和时间的国际标准。简化扩展 ISO 格式如下所示：

```
YYYY-MM-DDTHH:mm:ss.sssZ
```

其中：

- `YYYY` 表示年份（四位数）
- `MM` 表示月份（两位数）
- `DD` 表示日期（两位数）
- `T` 是分隔日期和时间的文字字符
- `HH` 表示小时（两位数）
- `mm` 表示分钟（两位数）
- `ss` 表示秒数（两位数）
- `sss` 表示毫秒（三位数）
- `Z` 表示协调世界时（UTC）时区（祖鲁时间）

例如，`2023-05-12T14:30:15.123Z` 表示 2023 年 5 月 12 日下午 2 点 30 分 15.123 秒（UTC 时间）。

## JavaScript 日期对象

JavaScript 提供了一个内置的 `Date` 对象，用于处理日期和时间。当你创建一个新的 `Date` 对象时，可以向其传递一个 ISO 格式的字符串：

```javascript
const date = new Date("2023-05-12T14:30:15.123Z");
```

让我们打开终端，练习使用日期对象：

1. 通过点击 WebIDE 顶部的“终端”菜单打开终端。
2. 输入 `node` 并按回车键，启动 Node.js 交互式 shell。
3. 创建一个表示当前时间的新日期对象：

```javascript
const now = new Date();
console.log(now);
```

![node-prompt](../assets/screenshot-20250306-odDaT5Rp@2x.png)

4. 将这个日期对象转换为 ISO 字符串：

```javascript
const isoString = now.toISOString();
console.log(isoString);
```

你应该会看到类似于以下的输出：

```
2023-05-12T14:30:15.123Z
```

5. 从 ISO 字符串创建一个日期对象：

```javascript
const dateFromIso = new Date("2023-05-12T14:30:15.123Z");
console.log(dateFromIso);
```

![node-prompt](../assets/screenshot-20250306-dbkCLkf7@2x.png)

这展示了 JavaScript 如何解析 ISO 格式的字符串并从中创建日期对象。
