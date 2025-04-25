# 计算两个日期之间的工作日

要计算两个日期之间的工作日，请执行以下步骤：

1. 打开终端/SSH 并输入`node`以开始练习编码。
2. 使用`Array.from()`创建一个长度等于`startDate`和`endDate`之间天数的数组。
3. 使用`Array.prototype.reduce()`遍历数组，检查每个日期是否为工作日，并增加`count`。
4. 在每次循环中使用`Date.prototype.getDate()`和`Date.prototype.setDate()`将`startDate`更新为下一天，使其前进一天。
5. 请注意，此函数未考虑法定节假日。

以下是实现此功能的代码：

```js
const countWeekDaysBetween = (startDate, endDate) =>
  Array.from({ length: (endDate - startDate) / (1000 * 3600 * 24) }).reduce(
    (count) => {
      if (startDate.getDay() % 6 !== 0) count++;
      startDate = new Date(startDate.setDate(startDate.getDate() + 1));
      return count;
    },
    0
  );
```

你可以使用以下代码测试该函数：

```js
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 06, 2020")); // 1
countWeekDaysBetween(new Date("Oct 05, 2020"), new Date("Oct 14, 2020")); // 7
```
