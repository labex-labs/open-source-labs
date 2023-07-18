# Function to Convert String to Snake Case

To convert a string to snake case, use the following function:

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

This function uses `String.prototype.match()` to break the string into words using an appropriate regular expression. Then, it uses `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, and `String.prototype.toLowerCase()` to combine the words, adding `_` as a separator.

Example usage:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); // 'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
