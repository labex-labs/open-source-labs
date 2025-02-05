# 用于计算过去日期的 JavaScript 函数

以下是一个 JavaScript 函数，它可以计算从今天起 `n` 天前的日期，并以 `yyyy-mm-dd` 格式的字符串返回：

```js
const daysAgo = (n) => {
  const today = new Date();
  const daysAgoDate = new Date(today.setDate(today.getDate() - Math.abs(n)));
  return daysAgoDate.toISOString().split("T")[0];
};
```

其工作原理如下：

- 使用 `Date` 构造函数获取当前日期。
- 使用 `Math.abs()` 函数确保天数为正数。
- 使用 `Date.prototype.getDate()` 函数获取当前日期的月份中的日期。
- 使用 `Date.prototype.setDate()` 函数相应地更新日期。
- 使用 `Date.prototype.toISOString()` 函数将结果日期以 `yyyy-mm-dd` 格式作为字符串返回。

示例用法：

```js
daysAgo(20); // "2020-09-16" （如果当前日期是 2020-10-06）
```
