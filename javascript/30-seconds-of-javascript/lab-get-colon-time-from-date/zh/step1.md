# 以下是如何从日期对象获取带冒号的时间

如果你想练习编码，可以先打开终端/SSH 并输入 `node`。

此函数从给定的 `Date` 对象返回格式为 `HH:MM:SS` 的字符串。

为实现这一点，利用了 `Date.prototype.toTimeString()` 和 `String.prototype.slice()` 方法来提取 `Date` 对象的 `HH:MM:SS` 部分。

以下是该函数的代码：

```js
const getColonTimeFromDate = (date) => date.toTimeString().slice(0, 8);
```

以下是一个使用示例：

```js
getColonTimeFromDate(new Date()); // '08:38:00'
```
