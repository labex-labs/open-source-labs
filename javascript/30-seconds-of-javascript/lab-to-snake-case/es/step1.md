# Función para convertir una cadena en formato snake case

Para convertir una cadena en formato snake case, utiliza la siguiente función:

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

Esta función utiliza `String.prototype.match()` para dividir la cadena en palabras utilizando una expresión regular adecuada. Luego, utiliza `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` y `String.prototype.toLowerCase()` para combinar las palabras, agregando `_` como separador.

Uso de ejemplo:

```js
toSnakeCase("camelCase"); // 'camel_case'
toSnakeCase("some text"); //'some_text'
toSnakeCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some_mixed_string_with_spaces_underscores_and_hyphens'
toSnakeCase("AllThe-small Things"); // 'all_the_small_things'
toSnakeCase("IAmEditingSomeXMLAndHTML");
// 'i_am_editing_some_xml_and_html'
```
