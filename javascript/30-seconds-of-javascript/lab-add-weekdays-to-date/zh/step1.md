# 向给定日期添加工作日的函数

要通过添加给定数量的工作日来计算未来日期，你可以使用 `addWeekDays` 函数。步骤如下：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `addWeekDays` 函数，该函数接受两个参数：`startDate` 和 `count`。
3. `startDate` 是你要开始添加工作日的日期。
4. `count` 是你要添加到起始日期的工作日数量。
5. 该函数使用 `Array.from()` 方法构造一个数组，并将其长度设置为要添加的工作日数量 `count`。
6. `Array.prototype.reduce()` 方法用于遍历数组，从 `startDate` 开始，并使用 `Date.prototype.getDate()` 和 `Date.prototype.setDate()` 对其进行递增。
7. 该函数检查当前 `date` 是否在周末。
8. 如果当前 `date` 在周末，该函数会通过添加一天或两天来再次更新它，使其成为工作日。
9. 该函数不考虑法定节假日。

```js
const addWeekDays = (startDate, count) =>
  Array.from({ length: count }).reduce((date) => {
    date = new Date(date.setDate(date.getDate() + 1));
    if (date.getDay() % 6 === 0)
      date = new Date(date.setDate(date.getDate() + (date.getDay() / 6 + 1)));
    return date;
  }, startDate);
```

以下是一些如何使用 `addWeekDays` 函数的示例：

```js
addWeekDays(new Date("Oct 09, 2020"), 5); // 'Oct 16, 2020'
addWeekDays(new Date("Oct 12, 2020"), 5); // 'Oct 19, 2020'
```
