# Función para convertir una cadena de texto (string) a formato Pascal case

Para convertir una cadena de texto a formato Pascal case, puedes utilizar la función `toPascalCase()`. Así es cómo hacerlo:

- Primero, abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
- Luego, utiliza el método `String.prototype.match()` con una expresión regular adecuada para dividir la cadena de texto en palabras.
- A continuación, utiliza los métodos `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toUpperCase()` y `String.prototype.toLowerCase()` para combinar las palabras, capitalizando la primera letra de cada palabra y convirtiendo el resto a minúsculas.
- Finalmente, llama a la función `toPascalCase()` con la cadena de texto deseada como argumento para convertirla a formato Pascal case.

Aquí está el código de la función `toPascalCase()`:

```js
const toPascalCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase())
    .join("");
```

Puedes utilizar esta función para convertir cualquier cadena de texto a formato Pascal case. Aquí hay algunos ejemplos:

```js
toPascalCase("some_database_field_name"); // 'SomeDatabaseFieldName'
toPascalCase("Some label that needs to be pascalized"); // 'SomeLabelThatNeedsToBePascalized'
toPascalCase("some-javascript-property"); // 'SomeJavascriptProperty'
toPascalCase("some-mixed_string with spaces_underscores-and-hyphens"); // 'SomeMixedStringWithSpacesUnderscoresAndHyphens'
```
