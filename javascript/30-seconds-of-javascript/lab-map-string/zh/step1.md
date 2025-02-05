# 用于映射字符串中字符的函数

要使用此函数来映射字符串中的字符，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 以开始练习编码。
- 使用 `String.prototype.split()` 和 `Array.prototype.map()` 对给定字符串中的每个字符调用提供的函数 `fn`。
- 使用 `Array.prototype.join()` 将字符数组重新组合成一个新字符串。
- 回调函数 `fn` 接受三个参数：当前字符、当前字符的索引以及调用 `mapString` 的字符串。

以下是函数代码：

```js
const mapString = (str, fn) =>
  str
    .split("")
    .map((c, i) => fn(c, i, str))
    .join("");
```

示例用法：

```js
mapString("lorem ipsum", (c) => c.toUpperCase()); // 'LOREM IPSUM'
```
