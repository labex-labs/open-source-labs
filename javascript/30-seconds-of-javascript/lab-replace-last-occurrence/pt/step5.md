# Criando um Módulo e Usando a Função

Nesta etapa final, converteremos nossa função em um módulo JavaScript adequado que pode ser importado e usado em outros arquivos. Esta é uma prática comum no desenvolvimento JavaScript do mundo real.

Primeiro, vamos criar um arquivo de módulo para nossa função. Crie um novo arquivo chamado `replaceLastModule.js` no diretório `replace-last`:

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

Agora, vamos criar outro arquivo para usar nosso módulo. Crie um novo arquivo chamado `app.js` no diretório `replace-last`:

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

Execute o aplicativo para ver como o módulo funciona:

```bash
node app.js
```

Você deve ver a saída com todos os exemplos demonstrando como a função `replaceLast` pode ser usada em vários cenários.

Parabéns. Você criou com sucesso uma função utilitária JavaScript útil e a empacotou como um módulo que pode ser reutilizado em seus projetos.
