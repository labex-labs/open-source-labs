# Creación de un módulo y uso de la función

En este último paso, convertiremos nuestra función en un módulo de JavaScript adecuado que se pueda importar y usar en otros archivos. Esta es una práctica común en el desarrollo de JavaScript en el mundo real.

Primero, creemos un archivo de módulo para nuestra función. Cree un nuevo archivo llamado `replaceLastModule.js` en el directorio `replace-last`:

```javascript
/**
 * Replaces the last occurrence of a pattern in a string.
 *
 * @param {string} str - The input string.
 * @param {string|RegExp} pattern - The pattern to replace (string or RegExp).
 * @param {string} replacement - The replacement string.
 * @returns {string} - The string with the last occurrence replaced.
 */
function replaceLast(str, pattern, replacement) {
  // Ensure str is a string
  if (typeof str !== "string") {
    return str;
  }

  // If str is empty or pattern is not provided, return original string
  if (str === "" || pattern === undefined) {
    return str;
  }

  // Ensure replacement is a string
  if (replacement === undefined) {
    replacement = "";
  } else if (typeof replacement !== "string") {
    replacement = String(replacement);
  }

  // Handle string patterns
  if (typeof pattern === "string") {
    const lastIndex = str.lastIndexOf(pattern);
    if (lastIndex === -1) {
      return str;
    }
    return (
      str.slice(0, lastIndex) +
      replacement +
      str.slice(lastIndex + pattern.length)
    );
  }

  // Handle regular expression patterns
  if (pattern instanceof RegExp) {
    // Create a global version of the regex to find all matches
    const globalRegex = new RegExp(
      pattern.source,
      "g" + (pattern.ignoreCase ? "i" : "") + (pattern.multiline ? "m" : "")
    );

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
    return (
      str.slice(0, lastIndex) +
      replacement +
      str.slice(lastIndex + lastMatch.length)
    );
  }

  // If pattern is neither string nor RegExp, return original string
  return str;
}

// Export the function
module.exports = replaceLast;
```

Ahora, creemos otro archivo para usar nuestro módulo. Cree un nuevo archivo llamado `app.js` en el directorio `replace-last`:

```javascript
// Import the replaceLast function
const replaceLast = require("./replaceLastModule");

// Examples of using the replaceLast function
console.log(
  "Example 1:",
  replaceLast("Hello world world", "world", "JavaScript")
);
console.log("Example 2:", replaceLast("abcabcabc", "abc", "123"));
console.log("Example 3:", replaceLast("file.txt.backup.txt", ".txt", ".md"));
console.log("Example 4:", replaceLast("123 456 789", /\d+/, "numbers"));
console.log(
  "Example 5:",
  replaceLast("The fox jumped over the lazy dog", /[a-z]+/i, "cat")
);

// Practical examples
const filePath = "/path/to/my/file.txt";
console.log("File with new extension:", replaceLast(filePath, ".txt", ".md"));

const url = "https://example.com/products/category/item?color=red";
console.log("URL with updated parameter:", replaceLast(url, "red", "blue"));

const htmlTag = "<div class='container'><p>Text</p></div>";
console.log(
  "HTML with replaced tag:",
  replaceLast(htmlTag, /<\/?\w+>/g, "<span>")
);
```

Ejecute la aplicación para ver cómo funciona el módulo:

```bash
node app.js
```

Debería ver la salida con todos los ejemplos que demuestran cómo se puede usar la función `replaceLast` en diversos escenarios.

Felicidades. Ha creado con éxito una útil función de utilidad de JavaScript y la ha empaquetado como un módulo que se puede reutilizar en sus proyectos.
