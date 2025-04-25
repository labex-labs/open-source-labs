# 如何从 Unix 时间戳创建日期对象

要从 Unix 时间戳创建一个 `Date` 对象，请按以下步骤操作：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 将时间戳乘以 `1000` 以将其转换为毫秒。
3. 使用 `Date` 构造函数创建一个新的 `Date` 对象。

以下是一个示例代码片段：

```js
const fromTimestamp = (timestamp) => new Date(timestamp * 1000);
```

你可以使用此函数将 Unix 时间戳转换为 `Date` 对象，如下所示：

```js
fromTimestamp(1602162242); // 2020-10-08T13:04:02.000Z
```
