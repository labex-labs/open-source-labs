# 返回月份最后一天的函数

要开始编码，请打开终端/SSH 并输入 `node`。

此函数返回给定日期所在月份的最后一天。

要实现这一点，请按以下步骤操作：

1. 使用 `Date.prototype.getFullYear()` 和 `Date.prototype.getMonth()` 从给定日期获取当前年份和月份。
2. 创建一个新日期，其年份和月份在给定的基础上加 `1`，日期设置为 `0`（上一个月的最后一天）。为此可以使用 `Date` 构造函数。
3. 如果没有向函数传递参数，它将默认使用当前日期。
4. 以日期的字符串表示形式返回月份的最后一天。

以下是该函数的代码：

```js
const getLastDateOfMonth = (date = new Date()) => {
  let lastDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
  return lastDate.toISOString().split("T")[0];
};
```

你可以通过像这样用一个日期对象调用该函数来测试它：

```js
getLastDateOfMonth(new Date("2015-08-11")); // '2015-08-30'
```
