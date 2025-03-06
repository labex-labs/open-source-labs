# Umgang mit regulären Ausdrücken (Regular Expressions)

Jetzt erweitern wir unsere Funktion, um auch reguläre Ausdrücke (Regular Expressions) zu verarbeiten. Wenn das Muster ein regulärer Ausdruck ist, müssen wir:

1. Alle Übereinstimmungen (matches) in der Zeichenfolge finden
2. Die letzte Übereinstimmung ermitteln
3. Diese letzte Übereinstimmung durch die Ersatzzeichenfolge ersetzen

Aktualisieren Sie Ihre `replaceLast`-Funktion, um reguläre Ausdrücke zu verarbeiten:

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

Fügen Sie Testfälle für reguläre Ausdrücke hinzu:

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

Führen Sie den Code erneut aus, um die aktualisierte Ausgabe zu sehen:

```bash
node replaceLast.js
```

Sowohl Zeichenfolgenmuster als auch reguläre Ausdrücke sollten jetzt in der `replaceLast`-Funktion korrekt funktionieren.
