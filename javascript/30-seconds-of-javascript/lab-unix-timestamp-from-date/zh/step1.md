# 如何在 JavaScript 中从日期获取 Unix 时间戳

要开始编码，请打开终端/SSH 并输入 `node`。

你可以使用以下步骤从 JavaScript 中的 `Date` 对象获取 Unix 时间戳：

1. 使用 `Date.prototype.getTime()` 获取以毫秒为单位的时间戳。
2. 将时间戳除以 `1000` 以获取以秒为单位的时间戳。
3. 使用 `Math.floor()` 将得到的时间戳四舍五入为整数。
4. 如果你省略 `date` 参数，将使用当前日期。

以下是一个示例代码片段：

```js
const getTimestamp = (date = new Date()) => Math.floor(date.getTime() / 1000);
```

你可以调用 `getTimestamp()` 函数来获取 Unix 时间戳。例如：

```js
getTimestamp(); // 1602162242
```
