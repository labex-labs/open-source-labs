# 为日期添加分钟数的函数

要为给定日期添加特定的分钟数，请使用以下函数：

```js
const addMinutesToDate = (date, n) => {
  // 根据给定日期创建一个Date对象
  const d = new Date(date);
  // 为Date对象添加n分钟
  d.setTime(d.getTime() + n * 60000);
  // 以yyyy-mm-dd HH:MM:SS格式返回新日期的字符串表示形式
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

要使用此函数，请将日期的字符串表示形式作为第一个参数传递，并将要添加（或减去，如果为负数）的分钟数作为第二个参数传递。例如：

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

请注意，该函数以`yyyy-mm-dd HH:MM:SS`格式将新日期作为字符串返回。
