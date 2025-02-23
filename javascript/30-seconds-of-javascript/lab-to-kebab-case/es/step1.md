# Convertir una cadena a formato kebab case

Para convertir una cadena a formato kebab case, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `String.prototype.match()` para dividir la cadena en palabras utilizando una expresión regular adecuada.
3. Utilice `Array.prototype.map()`, `Array.prototype.join()` y `String.prototype.toLowerCase()` para combinar las palabras, agregando `-` como separador.

A continuación, se muestra una función de ejemplo que realiza la conversión:

```js
const toKebabCase = (str) =>
  str &&
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.toLowerCase())
    .join("-");
```

Puede utilizar esta función para convertir cadenas a formato kebab case como se muestra a continuación:

```js
toKebabCase("camelCase"); // 'camel-case'
toKebabCase("some text"); //'some-text'
toKebabCase("some-mixed_string With spaces_underscores-and-hyphens");
//'some-mixed-string-with-spaces-underscores-and-hyphens'
toKebabCase("AllThe-small Things"); // 'all-the-small-things'
toKebabCase("IAmEditingSomeXMLAndHTML");
// 'i-am-editing-some-xml-and-html'
```
