# 如何将 3 位颜色代码扩展为 6 位颜色代码

要进行编码练习，请打开终端/SSH 并输入 `node`。你可以使用以下函数将 3 位颜色代码扩展为 6 位颜色代码：

```js
const extendHex = (shortHex) =>
  "#" +
  shortHex
    .slice(shortHex.startsWith("#") ? 1 : 0)
    .split("")
    .map((x) => x + x)
    .join("");
```

要将以 3 位表示的 RGB 十六进制颜色代码转换为 6 位形式，请执行以下步骤：

- 使用 `Array.prototype.map()`、`String.prototype.split()` 和 `Array.prototype.join()` 来连接映射后的数组。
- 使用 `Array.prototype.slice()` 从字符串开头移除 `#`，因为它只添加了一次。

以下是一些示例：

```js
extendHex("#03f"); // '#0033ff'
extendHex("05a"); // '#0055aa'
```
