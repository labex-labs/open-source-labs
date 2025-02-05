# 如何使用 Date 对象在 JavaScript 中获取一年中的第几天

要从 JavaScript 中的 `Date` 对象获取一年中的第几天（1 到 366 之间的数字），请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Date` 构造函数和 `Date.prototype.getFullYear()` 获取作为 `Date` 对象的一年中的第一天。
3. 从 `date` 对象中减去一年中的第一天，然后除以每天的毫秒数，以得到结果。
4. 使用 `Math.floor()` 将得到的天数四舍五入为整数。

以下是代码：

```js
const dayOfYear = (date) =>
  Math.floor((date - new Date(date.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
```

要测试该函数，请使用 `Date` 对象作为参数调用 `dayOfYear()`：

```js
dayOfYear(new Date()); // 272
```
