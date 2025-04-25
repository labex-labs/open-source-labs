# 检查闰年的代码

要检查给定的 `year` 是否为闰年，请执行以下步骤：

1. 打开终端/SSH。
2. 输入 `node` 开始编码。
3. 使用 `Date` 构造函数并将日期设置为给定 `year` 的 2 月 29 日。
4. 使用 `Date.prototype.getMonth()` 检查月份是否等于 `1`。
5. 使用以下代码片段检查一年是否为闰年：

```js
const isLeapYear = (year) => new Date(year, 1, 29).getMonth() === 1;
```

以下是如何使用此代码的示例：

```js
isLeapYear(2019); // false
isLeapYear(2020); // true
```
