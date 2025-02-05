# 用JavaScript从日期获取一年中的周数

要在JavaScript中获取与某个日期对应的一年中的零索引周数，请执行以下步骤：

1. 创建一个接受 `date` 参数的 `weekOfYear` 函数。
2. 使用 `Date` 构造函数和 `Date.prototype.getFullYear()` 以获取作为 `Date` 对象的一年中的第一天。
3. 结合使用 `Date.prototype.setDate()`、`Date.prototype.getDate()` 和 `Date.prototype.getDay()` 以及取模（`%`）运算符来获取一年中的第一个星期一。
4. 从给定的 `date` 中减去一年中的第一个星期一，并除以一周中的毫秒数。
5. 使用 `Math.round()` 来获取与给定 `date` 对应的一年中的零索引周数。
6. 如果给定的 `date` 在一年中的第一个星期一之前，则返回 `-0`。

以下是代码：

```js
const weekOfYear = (date) => {
  const startOfYear = new Date(date.getFullYear(), 0, 1);
  startOfYear.setDate(startOfYear.getDate() + (startOfYear.getDay() % 7));
  return Math.round((date - startOfYear) / (7 * 24 * 3600 * 1000));
};
```

要使用 `weekOfYear` 函数，只需将一个 `Date` 对象作为参数调用它：

```js
weekOfYear(new Date("2021-06-18")); // 23
```

这将返回与给定日期对应的一年中的零索引周数，在这种情况下是 `23`。
