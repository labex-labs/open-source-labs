# 将字符串转换为蛇形命名法的函数

要将字符串转换为蛇形命名法，请使用以下函数：

```js
const toSnakeCase = (str) => {
  if (!str) return "";
  const regex =
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
  return str
    .match(regex)
    .map((x) => x.toLowerCase())
    .join("_");
};
```

此函数使用 `String.prototype.match()` 通过适当的正则表达式将字符串拆分为单词。然后，它使用 `Array.prototype.map()`、`Array.prototype.slice()`、`Array.prototype.join()` 和 `String.prototype.toLowerCase()` 来组合这些单词，并添加 `_` 作为分隔符。

示例用法：

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); // 'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
