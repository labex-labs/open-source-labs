# 获取一个月天数的 JavaScript 函数

要使用 JavaScript 找出给定年份中特定月份的天数，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 创建一个名为 `daysInMonth` 的函数，该函数接受两个参数：`year`（年份）和 `month`（月份）。
3. 在 `daysInMonth` 函数内部，使用 `Date` 构造函数根据给定的 `year` 和 `month` 创建一个日期对象。
4. 将日期参数设置为 `0` 以获取上一个月的最后一天，因为月份是从 0 开始索引的。
5. 使用 `Date.prototype.getDate()` 返回给定 `month` 中的天数。
6. 从 `daysInMonth` 函数返回天数。

以下是 `daysInMonth` 函数的 JavaScript 代码：

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

你可以使用 `daysInMonth` 函数获取任何年份中任何月份的天数，如下例所示：

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
