# Optimisation de la fonction et test des cas limites

Notre fonction fonctionne pour les cas de base, mais optimisons-la et gérons certains cas limites :

1. Nous devrions vérifier si la chaîne de caractères d'entrée est vide.
2. Nous pouvons simplifier la gestion des expressions régulières (regex).
3. Nous devrions gérer les cas où le remplacement n'est pas une chaîne de caractères.

Mettez à jour votre fonction `replaceLast` avec ces optimisations :

```javascript
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
```

Ajoutons plus de cas de test pour couvrir les cas limites :

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)

// Test cases for regular expression patterns
console.log(replaceLast("Hello world world", /world/, "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("123 456 789", /\d+/, "numbers")); // Should output: "123 456 numbers"
console.log(replaceLast("abcdef", /xyz/, "123")); // Should output: "abcdef" (pattern not found)

// Edge cases
console.log(replaceLast("", "abc", "123")); // Should output: "" (empty string)
console.log(replaceLast("abcdef", "", "123")); // Should output: "abcde123f" (empty pattern)
console.log(replaceLast("abcdef", "def", "")); // Should output: "abc" (empty replacement)
console.log(replaceLast("AbCdEf", /[a-z]/, "X")); // Should output: "AbCdEX" (case-sensitive regex)
console.log(replaceLast("AbCdEf", /[a-z]/i, "X")); // Should output: "AbCdEX" (case-insensitive regex)
```

Exécutez le code à nouveau pour voir la sortie mise à jour :

```bash
node replaceLast.js
```

Cette version de la fonction gère plus de cas limites et maintient un code propre. Vous disposez maintenant d'une fonction `replaceLast` robuste prête à être utilisée dans vos projets.
