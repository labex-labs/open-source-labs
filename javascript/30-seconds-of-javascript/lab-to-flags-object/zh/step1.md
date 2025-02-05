# 将数组转换为标记对象

如果你想开始练习编码，请打开终端/SSH 并输入 `node`。

以下函数将字符串数组转换为映射为 `true` 的对象。

为此，我们使用 `Array.prototype.reduce()`。此方法将数组转换为一个对象，其中每个数组值都作为一个键，其值设置为 `true`。

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

下面是一个示例：

```js
flags(["red", "green"]); // { red: true, green: true }
```
