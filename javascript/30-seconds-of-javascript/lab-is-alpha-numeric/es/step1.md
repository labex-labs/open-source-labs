# Comprender los caracteres alfanuméricos

Los caracteres alfanuméricos consisten en las 26 letras del alfabeto inglés (tanto mayúsculas A-Z como minúsculas a-z) y los 10 dígitos numéricos (0-9). Cuando verificamos si una cadena es alfanumérica, estamos comprobando que solo contenga estos caracteres y nada más.

En JavaScript, podemos comprobar los caracteres alfanuméricos utilizando expresiones regulares. Las expresiones regulares (regex) son patrones utilizados para coincidir con combinaciones de caracteres en cadenas.

Comencemos abriendo nuestro editor de código. En el WebIDE, navega hasta el explorador de archivos en el lado izquierdo y crea un nuevo archivo JavaScript:

1. Haz clic derecho en el panel del explorador de archivos.
2. Selecciona "Nuevo archivo".
3. Nombrar el archivo `alphanumeric.js`.

Una vez que hayas creado el archivo, debería abrirse automáticamente en el editor. Si no es así, haz clic en `alphanumeric.js` en el explorador de archivos para abrirlo.

![new-file](../assets/screenshot-20250306-K5AOWF7Z@2x.png)

Ahora, ingresemos el siguiente código:

```javascript
// Function to check if a string is alphanumeric
function isAlphaNumeric(str) {
  // Using regular expression to check for alphanumeric characters
  return /^[a-zA-Z0-9]+$/.test(str);
}

// Example usage
console.log("Is 'hello123' alphanumeric?", isAlphaNumeric("hello123"));
console.log("Is '123' alphanumeric?", isAlphaNumeric("123"));
console.log("Is 'hello 123' alphanumeric?", isAlphaNumeric("hello 123"));
console.log("Is 'hello@123' alphanumeric?", isAlphaNumeric("hello@123"));
```

Guarda el archivo presionando `Ctrl+S` o seleccionando "Archivo" > "Guardar" desde el menú.

Ahora, ejecutemos este archivo JavaScript para ver la salida. Abre la terminal en el WebIDE seleccionando "Terminal" > "Nueva terminal" desde el menú o presionando `` Ctrl+` ``.

En la terminal, ejecuta el siguiente comando:

```bash
node alphanumeric.js
```

Deberías ver la siguiente salida:

```
Is 'hello123' alphanumeric? true
Is '123' alphanumeric? true
Is 'hello 123' alphanumeric? false
Is 'hello@123' alphanumeric? false
```

Esta salida muestra que nuestra función identifica correctamente `hello123` y `123` como cadenas alfanuméricas, mientras que `hello 123` (contiene un espacio) y `hello@123` (contiene un carácter especial @) no son alfanuméricas.
