# 计算日期差值（以秒为单位）的函数

要以秒为单位计算两个日期之间的差值，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 用两个 `Date` 对象相减，再除以一秒中的毫秒数。
3. 结果将是以秒为单位的两个日期之间的差值。

以下是一个执行此计算的 JavaScript 函数：

```js
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

要使用此函数，请传入两个 `Date` 对象作为参数，如下所示：

```js
getSecondsDiffBetweenDates(
  new Date("2020-12-24 00:00:15"),
  new Date("2020-12-24 00:00:17")
); // 2
```
