# 格式化持续时间

要获取给定毫秒数的人类可读格式，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 将 `ms` 除以适当的值，以获得 `天`、`小时`、`分钟`、`秒` 和 `毫秒` 的适当值。
3. 将 `Object.entries()` 与 `Array.prototype.filter()` 一起使用，仅保留非零值。
4. 使用 `Array.prototype.map()` 为每个值创建字符串，并适当地使用复数形式。
5. 使用 `Array.prototype.join()` 将这些值组合成一个字符串。

以下是代码：

```js
const formatDuration = (ms) => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter((val) => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? "s" : ""}`)
    .join(", ");
};
```

以下是一些示例：

```js
formatDuration(1001); // '1 秒，1 毫秒'
formatDuration(34325055574);
// '397 天，6 小时，44 分钟，15 秒，574 毫秒'
```
