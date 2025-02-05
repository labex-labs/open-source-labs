# 获取明天的日期

为了练习编码，你可以先打开终端/SSH 并输入 `node`。完成此操作后，你可以通过以下步骤获取明天的日期：

1. 使用 `Date` 构造函数获取当前日期。
2. 使用 `Date.prototype.getDate()` 将其加 1。
3. 使用 `Date.prototype.setDate()` 将值设置为结果。
4. 使用 `Date.prototype.toISOString()` 返回 `yyyy - mm - dd` 格式的字符串。

以下是你可以使用的代码：

```js
const tomorrow = () => {
  let currentDate = new Date();
  currentDate.setDate(currentDate.getDate() + 1);
  return currentDate.toISOString().split("T")[0];
};
```

输入此代码后，你可以通过调用函数 `tomorrow()` 获取明天的日期。例如，如果今天的日期是 2018 - 10 - 18，输出将是 `2018 - 10 - 19`。
