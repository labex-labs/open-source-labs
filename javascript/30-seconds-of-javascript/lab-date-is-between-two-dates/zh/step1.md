# 检查一个日期是否在另外两个日期之间

要检查一个日期是否在另外两个日期之间，可以在 JavaScript 中使用大于（`>`）和小于（`<`）运算符。以下是一个示例函数：

```js
const isBetweenDates = (dateStart, dateEnd, date) =>
  date > dateStart && date < dateEnd;
```

要使用此函数，请传入开始日期、结束日期和要检查的日期。如果该日期在开始日期和结束日期之间，函数将返回 `true`，否则返回 `false`。以下是一些示例：

```js
isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 19)
); // false

isBetweenDates(
  new Date(2010, 11, 20),
  new Date(2010, 11, 30),
  new Date(2010, 11, 25)
); // true
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
