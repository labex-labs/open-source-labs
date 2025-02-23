# Conversión de cadenas a camelCase

Para convertir una cadena a camelCase, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `String.prototype.match()` con una expresión regular adecuada para dividir la cadena en palabras.
3. Utilice `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toLowerCase()` y `String.prototype.toUpperCase()` para combinar las palabras y poner en mayúscula la primera letra de cada una.
4. Utilice la función `toCamelCase` que se muestra a continuación para realizar la conversión:

```js
const toCamelCase = (str) => {
  const words =
    str &&
    str.match(
      /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
    );
  const capitalizedWords =
    words &&
    words.map(
      (word) => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase()
    );
  const camelCaseString = capitalizedWords && capitalizedWords.join("");
  return (
    camelCaseString &&
    camelCaseString.slice(0, 1).toLowerCase() + camelCaseString.slice(1)
  );
};
```

A continuación se presentan algunos ejemplos de cómo utilizar la función `toCamelCase`:

```js
toCamelCase("some_database_field_name"); //'someDatabaseFieldName'
toCamelCase("Some label that needs to be camelized");
//'someLabelThatNeedsToBeCamelized'
toCamelCase("some-javascript-property"); //'someJavascriptProperty'
toCamelCase("some-mixed_string with spaces_underscores-and-hyphens");
//'someMixedStringWithSpacesUnderscoresAndHyphens'
```
