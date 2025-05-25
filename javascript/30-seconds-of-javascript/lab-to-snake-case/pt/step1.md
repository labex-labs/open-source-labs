# Função para Converter String para Snake Case

Para converter uma string para snake case, use a seguinte função:

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

Esta função usa `String.prototype.match()` para quebrar a string em palavras usando uma expressão regular apropriada. Em seguida, ela usa `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` e `String.prototype.toLowerCase()` para combinar as palavras, adicionando `_` como um separador.

Exemplo de uso:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); // 'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
// 'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
