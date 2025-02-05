# 将字符串转换为标题大小写的函数

要将给定字符串转换为标题大小写，请使用以下函数。它使用 `String.prototype.match()` 通过适当的正则表达式将字符串拆分为单词。然后使用 `Array.prototype.map()`、`Array.prototype.slice()`、`Array.prototype.join()` 和 `String.prototype.toUpperCase()` 将它们组合起来。这会将每个单词的首字母大写，并在它们之间添加一个空格。

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

以下是一些使用该函数的示例：

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
