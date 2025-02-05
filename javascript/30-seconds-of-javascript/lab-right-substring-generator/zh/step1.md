# 右侧子字符串生成器

要生成给定字符串的所有右侧子字符串，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 如果字符串为空，则使用 `String.prototype.length` 提前停止迭代。
3. 使用 `for...in` 循环和 `String.prototype.slice()` 从末尾开始 `yield` 给定字符串的每个子字符串。

以下是代码片段：

```js
const rightSubstrGenerator = function* (str) {
  if (!str.length) return;
  for (let i in str) yield str.slice(-i - 1);
};
```

示例用法：

```js
[...rightSubstrGenerator("hello")];
// [ 'o', 'lo', 'llo', 'ello', 'hello' ]
```
