# Función para convertir una cadena a formato título

Para convertir una cadena dada a formato título, utiliza la siguiente función. Utiliza `String.prototype.match()` para dividir la cadena en palabras utilizando una expresión regular adecuada. Luego las combina utilizando `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` y `String.prototype.toUpperCase()`. Esto capitaliza la primera letra de cada palabra y agrega un espacio en blanco entre ellas.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

A continuación, se presentan algunos ejemplos de cómo utilizar la función:

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
