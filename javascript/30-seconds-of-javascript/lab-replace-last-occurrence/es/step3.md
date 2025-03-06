# Manejando patrones de expresiones regulares

Ahora, mejoremos nuestra función para manejar patrones de expresiones regulares. Cuando el patrón es una expresión regular, necesitamos:

1. Encontrar todas las coincidencias en la cadena.
2. Obtener la última coincidencia.
3. Reemplazar esa última coincidencia con la cadena de reemplazo.

Actualice su función `replaceLast` para manejar patrones de expresiones regulares:

```javascript
function replaceLast(str, pattern, replacement) {
  // Ensure inputs are valid
  if (typeof str !== "string") {
    return str;
  }

  // Handle string patterns
  if (typeof pattern === "string") {
    const lastIndex = str.lastIndexOf(pattern);
    if (lastIndex === -1) {
      return str;
    }
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + pattern.length);
    return before + replacement + after;
  }

  // Handle regular expression patterns
  if (pattern instanceof RegExp) {
    // Create a new RegExp with global flag to find all matches
    const globalRegex = new RegExp(pattern.source, "g");

    // Find all matches
    const matches = str.match(globalRegex);

    // If no matches, return original string
    if (!matches || matches.length === 0) {
      return str;
    }

    // Get the last match
    const lastMatch = matches[matches.length - 1];

    // Find the position of the last match
    const lastIndex = str.lastIndexOf(lastMatch);

    // Rebuild the string with the replacement
    const before = str.slice(0, lastIndex);
    const after = str.slice(lastIndex + lastMatch.length);
    return before + replacement + after;
  }

  // If pattern is neither string nor RegExp, return original string
  return str;
}
```

Agregue casos de prueba para patrones de expresiones regulares:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)

// Test cases for regular expression patterns
console.log(replaceLast("Hello world world", /world/, "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("123 456 789", /\d+/, "numbers")); // Should output: "123 456 numbers"
console.log(replaceLast("abcdef", /xyz/, "123")); // Should output: "abcdef" (pattern not found)
```

Ejecute el código nuevamente para ver la salida actualizada:

```bash
node replaceLast.js
```

Tanto los patrones de cadenas como los patrones de expresiones regulares ahora deberían funcionar correctamente en la función `replaceLast`.
