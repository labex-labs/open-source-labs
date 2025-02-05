# 以 yyyy - mm - dd 格式获取昨天的日期

要以 `yyyy - mm - dd` 格式获取昨天的日期，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `Date` 构造函数获取当前日期。
3. 使用 `Date.prototype.getDate()` 将日期减一。
4. 使用 `Date.prototype.setDate()` 设置减一之后的日期。
5. 使用 `Date.prototype.toISOString()` 返回 `yyyy - mm - dd` 格式的字符串。
6. 调用函数 `yesterday()` 以获取昨天的日期。

```js
const yesterday = () => {
  let d = new Date();
  d.setDate(d.getDate() - 1);
  return d.toISOString().split("T")[0];
};

yesterday(); // 如果当前日期是 2018 - 10 - 18，则返回 "2018 - 10 - 17"
```

按照这些步骤操作，你将能够以清晰简洁的方式获取昨天的日期。
