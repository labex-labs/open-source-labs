# 用于检查字符串是否以子字符串结尾的函数

要检查给定字符串是否以另一个字符串的子字符串结尾，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `for...in` 循环和 `String.prototype.slice()` 从给定 `word` 的末尾开始获取每个子字符串。
3. 使用 `String.prototype.endsWith()` 将当前子字符串与 `text` 进行比较。
4. 如果找到匹配的子字符串，则返回该子字符串。否则，返回 `undefined`。

以下是实现上述步骤的代码片段：

```js
const endsWithSubstring = (text, word) => {
  for (let i in word) {
    const substr = word.slice(0, i + 1);
    if (text.endsWith(substr)) return substr;
  }
  return undefined;
};
```

你可以使用以下示例测试该函数：

```js
endsWithSubstring("Lorem ipsum dolor sit amet<br /", "<br />"); // '<br /'
```
