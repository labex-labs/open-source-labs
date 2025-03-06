# Optimierung der Funktion und Testen von Randfällen

Unsere Funktion funktioniert für grundlegende Fälle, aber lassen Sie uns sie optimieren und einige Randfälle behandeln:

1. Wir sollten prüfen, ob die Eingabezeichenfolge leer ist.
2. Wir können die Verarbeitung von regulären Ausdrücken vereinfachen.
3. Wir sollten Fälle behandeln, in denen der Ersatzwert keine Zeichenfolge ist.

Aktualisieren Sie Ihre `replaceLast`-Funktion mit diesen Optimierungen:

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

Fügen Sie weitere Testfälle hinzu, um die Randfälle abzudecken:

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

Führen Sie den Code erneut aus, um die aktualisierte Ausgabe zu sehen:

```bash
node replaceLast.js
```

Diese Version der Funktion behandelt mehr Randfälle und behält sauberen Code. Sie haben jetzt eine robuste `replaceLast`-Funktion, die Sie in Ihren Projekten verwenden können.
