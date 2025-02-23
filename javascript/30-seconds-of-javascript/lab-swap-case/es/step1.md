# Cómo intercambiar el caso de una cadena en JavaScript

Para intercambiar el caso de una cadena en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador spread (`...`) para convertir la cadena de entrada `str` en una matriz de caracteres.
3. Utilice `String.prototype.toLowerCase()` y `String.prototype.toUpperCase()` para convertir los caracteres en minúsculas a mayúsculas y viceversa.
4. Utilice `Array.prototype.map()` para aplicar la transformación a cada carácter y `Array.prototype.join()` para combinar los caracteres de nuevo en una cadena.
5. Tenga en cuenta que intercambiar el caso de una cadena dos veces no necesariamente resultará en la cadena original.

A continuación, se muestra un fragmento de código de ejemplo que demuestra cómo intercambiar el caso de una cadena en JavaScript:

```js
const swapCase = (str) =>
  [...str]
    .map((c) => (c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))
    .join("");

swapCase("Hello world!"); // Salida: 'hELLO WORLD!'
```
