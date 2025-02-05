# 计算从今天起 `n` 天后日期的函数

要计算从今天起 `n` 天后的日期，请按以下步骤操作：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `Date` 构造函数获取当前日期。
- 使用 `Math.abs()` 和 `Date.prototype.getDate()` 相应地更新日期。
- 使用 `Date.prototype.setDate()` 设置结果。
- 使用 `Date.prototype.toISOString()` 返回 `yyyy-mm-dd` 格式的字符串。

以下是代码：

```js
const daysFromNow = (n) => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + Math.abs(n));
  return currentDate.toISOString().split("T")[0];
};
```

示例用法：

```js
daysFromNow(5); // 输出：2020-10-13（如果当前日期是 2020-10-08）
```
