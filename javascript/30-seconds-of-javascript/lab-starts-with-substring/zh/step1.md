# 检查字符串是否以子串开头的函数

要检查给定字符串是否以另一个字符串的子串开头，请执行以下步骤：

- 打开终端/SSH 并输入 `node` 开始练习编码。
- 使用 `for...in` 循环和 `String.prototype.slice()` 方法从开头获取给定 `word` 的每个子串。
- 使用 `String.prototype.startsWith()` 方法将当前子串与 `text` 进行比较。
- 如果找到匹配的子串，则返回它。否则，返回 `undefined`。

以下是一个实现此功能的 JavaScript 函数：

```js
const startsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(-i - 1);
    if (text.startsWith(substr)) return substr;
  }
  return undefined;
};
```

你可以按如下方式调用此函数：

```js
startsWithSubstring("/>Lorem ipsum dolor sit amet", "<br />"); // 返回 '/>'
```
