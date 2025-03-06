# Création d'un module et utilisation de la fonction

Dans cette étape finale, nous allons convertir notre fonction en un véritable module JavaScript qui peut être importé et utilisé dans d'autres fichiers. C'est une pratique courante dans le développement JavaScript dans le monde réel.

Tout d'abord, créons un fichier de module pour notre fonction. Créez un nouveau fichier appelé `replaceLastModule.js` dans le répertoire `replace-last` :

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

Maintenant, créons un autre fichier pour utiliser notre module. Créez un nouveau fichier appelé `app.js` dans le répertoire `replace-last` :

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

Exécutez l'application pour voir comment le module fonctionne :

```bash
node app.js
```

Vous devriez voir la sortie avec tous les exemples montrant comment la fonction `replaceLast` peut être utilisée dans diverses situations.

Félicitations. Vous avez créé avec succès une fonction utilitaire JavaScript utile et l'avez emballée en tant que module qui peut être réutilisé dans vos projets.
