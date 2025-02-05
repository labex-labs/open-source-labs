# 将字符串转换为短横线命名法

要将字符串转换为短横线命名法，请执行以下步骤：

1. 打开终端/SSH 并输入 `node` 以开始练习编码。
2. 使用 `String.prototype.match()` 通过适当的正则表达式将字符串拆分为单词。
3. 使用 `Array.prototype.map()`、`Array.prototype.join()` 和 `String.prototype.toLowerCase()` 来组合单词，并添加 `-` 作为分隔符。

以下是一个执行转换的示例函数：

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

你可以使用此函数将字符串转换为短横线命名法，如下所示：

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); // 'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
