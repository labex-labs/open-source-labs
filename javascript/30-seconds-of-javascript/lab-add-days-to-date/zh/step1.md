# 给日期添加天数的函数

这里有一个函数，它可以计算从给定日期起 `n` 天后的日期，并返回其字符串表示形式。

要使用该函数，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Date` 构造函数从第一个参数创建一个 `Date` 对象。
3. 使用 `Date.prototype.getDate()` 和 `Date.prototype.setDate()` 给给定日期添加 `n` 天。
4. 使用 `Date.prototype.toISOString()` 以 `yyyy - mm - dd` 格式返回一个字符串。

以下是该函数的代码：

```js
const addDaysToDate = (date, n) => {
  const d = new Date(date);
  d.setDate(d.getDate() + n);
  return d.toISOString().split("T")[0];
};
```

你可以使用以下示例测试该函数：

```js
addDaysToDate("2020-10-15", 10); // '2020-10-25'
addDaysToDate("2020-10-15", -10); // '2020-10-05'
```
