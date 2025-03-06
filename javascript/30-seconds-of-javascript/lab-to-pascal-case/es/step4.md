# Crear la Función Completa toPascalCase

Ahora que entendemos todos los componentes necesarios, creemos una función completa `toPascalCase` que pueda manejar cualquier cadena de texto de entrada.

1. Creemos un archivo de JavaScript para guardar nuestra función. Salga de su sesión de Node.js presionando Ctrl+C dos veces o escribiendo `.exit`.

2. En el WebIDE, cree un nuevo archivo haciendo clic en "File" > "New File" en el menú superior.

3. Guarde el archivo como `pascalCase.js` en el directorio `/home/labex/project`.

4. Copie y pegue el siguiente código en el editor:

```javascript
/**
 * Converts a string to Pascal case.
 * @param {string} str - The input string to convert.
 * @returns {string} The Pascal cased string.
 */
function toPascalCase(str) {
  // Use regex to match words regardless of delimiter
  const words = str.match(
    /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
  );

  // If no words are found, return an empty string
  if (!words) {
    return "";
  }

  // Capitalize each word and join them
  return words
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// Test cases
console.log(toPascalCase("hello world")); // "HelloWorld"
console.log(toPascalCase("some_database_field_name")); // "SomeDatabaseFieldName"
console.log(toPascalCase("Some label that needs to be pascalized")); // "SomeLabelThatNeedsToBePascalized"
console.log(toPascalCase("some-javascript-property")); // "SomeJavascriptProperty"
console.log(
  toPascalCase("some-mixed_string with spaces_underscores-and-hyphens")
); // "SomeMixedStringWithSpacesUnderscoresAndHyphens"
```

5. Guarde el archivo presionando Ctrl+S o seleccionando "File" > "Save" del menú.

6. Ejecute el archivo utilizando Node.js abriendo la Terminal y escribiendo:

```bash
node pascalCase.js
```

Debería ver la siguiente salida:

```
HelloWorld
SomeDatabaseFieldName
SomeLabelThatNeedsToBePascalized
SomeJavascriptProperty
SomeMixedStringWithSpacesUnderscoresAndHyphens
```

Nuestra función `toPascalCase` ahora está funcionando correctamente. Revisemos cómo funciona:

1. Utilizamos una expresión regular para encontrar coincidencias de palabras en la cadena de texto de entrada, independientemente de los delimitadores utilizados.
2. Verificamos si se encontraron palabras. Si no, devolvemos una cadena vacía.
3. Utilizamos `map()` para poner en mayúsculas cada palabra y `join('')` para combinarlas sin separadores.
4. El resultado es una cadena de texto en Pascal Case donde cada palabra comienza con una letra mayúscula y el resto están en minúsculas.
