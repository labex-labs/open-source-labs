# 如何在 JavaScript 中将制表符转换为空格

在编码时将制表符转换为空格，请遵循以下步骤：

1. 打开终端/SSH 并输入 `node` 开始练习编码。
2. 使用 `String.prototype.replace()` 方法、正则表达式和 `String.prototype.repeat()`，将每个制表符替换为所需数量的空格。
3. 以下代码片段展示了如何使用 `expandTabs` 函数将制表符替换为空格：

```js
const expandTabs = (str, count) => str.replace(/\t/g, " ".repeat(count));

expandTabs("\t\tlorem", 3); // '      lorem'
```

在上述示例中，`expandTabs` 函数接受两个参数：一个包含制表符的字符串 `str`，以及一个数字 `count`，表示用多少个空格替换每个制表符。该函数使用 `String.prototype.replace()` 方法和正则表达式 (`/\t/g`) 来查找输入字符串中的所有制表符，并使用 `String.prototype.repeat()` 方法将它们替换为所需数量的空格。
