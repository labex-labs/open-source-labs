# 计算日期天数差的函数

要计算两个日期之间的天数差，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `getDaysDiffBetweenDates` 函数，并将两个 `Date` 对象作为参数传入。
3. 该函数会用结束日期减去开始日期，然后将结果除以一天中的毫秒数，以得到它们之间的天数差。

以下是 `getDaysDiffBetweenDates` 函数的代码：

```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);
```

要使用该函数，请传入两个格式为 `YYYY-MM-DD` 的 `Date` 对象：

```js
getDaysDiffBetweenDates(new Date("2017-12-13"), new Date("2017-12-22")); // 9
```

这将返回两个日期之间的天数差，在此示例中为 9 天。
