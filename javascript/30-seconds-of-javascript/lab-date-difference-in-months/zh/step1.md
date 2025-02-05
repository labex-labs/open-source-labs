# 计算月份日期差的函数

要计算两个日期之间的月份差，请使用以下函数：

```js
const getMonthsDiffBetweenDates = (dateInitial, dateFinal) =>
  Math.max(
    (dateFinal.getFullYear() - dateInitial.getFullYear()) * 12 +
      dateFinal.getMonth() -
      dateInitial.getMonth(),
    0
  );
```

要使用此函数，请将两个 `Date` 对象作为参数传递。例如：

```js
getMonthsDiffBetweenDates(new Date("2017-12-13"), new Date("2018-04-29")); // 4
```

此函数使用 `Date.prototype.getFullYear()` 和 `Date.prototype.getMonth()` 方法来计算两个日期之间的月份差。
