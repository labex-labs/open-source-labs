# Comprendiendo el problema y configurando el entorno

Antes de comenzar a codificar, entendamos qué debe hacer nuestra función `replaceLast`:

1. Aceptar tres parámetros:
   - `str`: La cadena de entrada que se va a modificar
   - `pattern`: La subcadena o expresión regular a buscar
   - `replacement`: La cadena con la que se reemplazará la última aparición

2. Devolver una nueva cadena con la última aparición del patrón reemplazada.

Creemos un archivo JavaScript para implementar nuestra función:

1. Navegue hasta el directorio del proyecto en el explorador de archivos de WebIDE.
2. Cree un nuevo archivo llamado `replaceLast.js` en el directorio `replace-last`.
3. Agregue la siguiente estructura básica al archivo:

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

Para comprobar que todo está configurado correctamente, agreguemos una prueba simple:

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

Ahora, ejecutemos nuestro código para ver la salida actual:

1. Abra la Terminal en WebIDE
2. Navegue hasta el directorio `replace-last`:
   ```bash
   cd ~/project/replace-last
   ```
3. Ejecute el archivo JavaScript utilizando Node.js:
   ```bash
   node replaceLast.js
   ```

Debería ver `Hello world world` en la salida porque nuestra función actualmente solo devuelve la cadena original sin realizar ningún cambio.
