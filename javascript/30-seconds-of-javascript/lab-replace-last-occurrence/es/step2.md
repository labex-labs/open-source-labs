# Implementando la lógica central de la función

Ahora que comprendemos el problema, implementemos la funcionalidad central de nuestra función `replaceLast`. Nos centraremos primero en manejar patrones de cadenas y luego abordaremos las expresiones regulares en el siguiente paso.

Cuando el patrón es una cadena, podemos usar el método `lastIndexOf` para encontrar la posición de la última aparición. Una vez que conocemos esta posición, podemos usar el método `slice` para reconstruir la cadena insertando el reemplazo.

Actualice su función `replaceLast` con la siguiente implementación:

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  if (typeof pattern === "string") {
    // Find the position of the last occurrence
    const lastIndex = str.lastIndexOf(pattern);

    // If pattern not found, return original string
    if (lastIndex === -1) {
      return str;
    }

    // Rebuild the string with the replacement
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // We'll handle regex patterns in the next step
  return str;
}
```

Actualice sus casos de prueba para verificar que la función maneje correctamente los patrones de cadenas:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

Ejecute el código nuevamente para ver la salida actualizada:

```bash
node replaceLast.js
```

Ahora debería ver la última aparición del patrón de cadena reemplazada en cada caso de prueba. Por ejemplo, "Hello world JavaScript" en lugar de "Hello world world".
