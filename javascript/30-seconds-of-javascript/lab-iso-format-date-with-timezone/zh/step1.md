# 将日期转换为带时区的 ISO 格式

要将日期转换为扩展的 ISO 格式（ISO 8601），包括时区偏移，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始编码。
2. 使用 `Date.prototype.getTimezoneOffset()` 获取时区偏移并将其反转。将其符号存储在 `diff` 中。
3. 定义一个辅助函数 `pad()`，它使用 `Math.floor()` 和 `Math.abs()` 将任何传入的数字规范化为整数，并使用 `String.prototype.padStart()` 将其填充为两位数。
4. 使用 `pad()` 和 `Date` 原型中的内置方法来构建带有时区偏移的 ISO 8601 字符串。

以下是你可以使用的代码：

```js
const toISOStringWithTimezone = (date) => {
  const tzOffset = -date.getTimezoneOffset();
  const diff = tzOffset >= 0 ? "+" : "-";
  const pad = (n) => `${Math.floor(Math.abs(n))}`.padStart(2, "0");
  return (
    date.getFullYear() +
    "-" +
    pad(date.getMonth() + 1) +
    "-" +
    pad(date.getDate()) +
    "T" +
    pad(date.getHours()) +
    ":" +
    pad(date.getMinutes()) +
    ":" +
    pad(date.getSeconds()) +
    diff +
    pad(tzOffset / 60) +
    ":" +
    pad(tzOffset % 60)
  );
};
```

使用函数 `toISOStringWithTimezone()`，并将一个 `new Date()` 对象作为参数，以获取带时区偏移的 ISO 格式日期。例如：

```js
toISOStringWithTimezone(new Date()); // '2020-10-06T20:43:33-04:00'
```
