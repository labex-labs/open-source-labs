# 计算日期差值（以分钟为单位）的函数

要计算两个日期之间的差值（以分钟为单位），请使用以下函数：

```js
const getMinutesDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 60);
```

只需将两个 `Date` 对象相减，再除以一分钟内的毫秒数，即可得到它们之间的差值（以分钟为单位）。

以下是该函数的一个示例用法：

```js
getMinutesDiffBetweenDates(
  new Date("2021-04-24 01:00:15"),
  new Date("2021-04-24 02:00:15")
); // 60
```

要开始练习编码，请打开终端/SSH 并输入 `node`。
