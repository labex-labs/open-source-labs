# 理解 JavaScript 中的日期计算

既然我们已经了解了如何创建 `Date` 对象，接下来就学习如何计算两个日期之间的差值。

## JavaScript 中的日期运算

JavaScript 允许你直接对 `Date` 对象执行算术运算。当你用一个 `Date` 对象减去另一个 `Date` 对象时，JavaScript 会自动将它们转换为时间戳（毫秒），然后进行减法运算。

```javascript
let date1 = new Date("2023-01-01T00:00:00");
let date2 = new Date("2023-01-01T00:01:00");

let differenceInMilliseconds = date2 - date1;
console.log(differenceInMilliseconds); // 60000 (60 秒 * 1000 毫秒)
```

在你的 Node.js 环境中运行这段代码。结果应该是 `60000`，它表示 60 秒对应的毫秒数。

## 将毫秒转换为秒

要将时间差从毫秒转换为秒，只需将毫秒数除以 1000：

```javascript
let differenceInSeconds = differenceInMilliseconds / 1000;
console.log(differenceInSeconds); // 60
```

这样我们就得到了以秒为单位的时间差，在这个例子中是 60 秒，即 1 分钟。

## 创建日期差值函数

既然我们已经理解了这个概念，那就创建一个简单的函数来计算两个日期之间的秒数差：

```javascript
function getDateDifferenceInSeconds(startDate, endDate) {
  return (endDate - startDate) / 1000;
}

// 测试函数
let start = new Date("2023-01-01T00:00:00");
let end = new Date("2023-01-01T00:01:30");
let difference = getDateDifferenceInSeconds(start, end);
console.log(difference); // 90 (1 分钟 30 秒)
```

在 Node.js 环境中输入并执行这个函数。结果应该是 `90`，表示 1 分钟 30 秒。
