# 用于计算日期小时数差异的 JavaScript 函数

要使用 JavaScript 计算两个日期之间的小时数差异，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。

2. 使用以下 JavaScript 函数获取两个 `Date` 对象之间的差异（以小时为单位）：

```js
const getHoursDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600);
```

3. 将两个日期作为参数调用该函数以获取小时数差异：

```js
getHoursDiffBetweenDates(
  new Date("2021-04-24 10:25:00"),
  new Date("2021-04-25 10:25:00")
); // 24
```
