# Implementierung der Kernfunktionslogik

Nachdem wir das Problem verstanden haben, implementieren wir nun die Kernfunktionalität unserer `replaceLast`-Funktion. Zunächst konzentrieren wir uns auf die Verarbeitung von Zeichenfolgenmustern (string patterns), und im nächsten Schritt werden wir uns mit regulären Ausdrücken (Regular Expressions) befassen.

Wenn das Muster eine Zeichenfolge ist, können wir die `lastIndexOf`-Methode verwenden, um die Position des letzten Vorkommens zu finden. Sobald wir diese Position kennen, können wir die `slice`-Methode nutzen, um die Zeichenfolge mit dem eingefügten Ersatz neu aufzubauen.

Aktualisieren Sie Ihre `replaceLast`-Funktion mit der folgenden Implementierung:

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

Aktualisieren Sie Ihre Testfälle, um zu überprüfen, ob die Funktion Zeichenfolgenmuster korrekt verarbeitet:

```javascript
// Test cases for string patterns
console.log(replaceLast("Hello world world", "world", "JavaScript")); // Should output: "Hello world JavaScript"
console.log(replaceLast("abcabcabc", "abc", "123")); // Should output: "abcabc123"
console.log(replaceLast("abcdef", "xyz", "123")); // Should output: "abcdef" (pattern not found)
```

Führen Sie den Code erneut aus, um die aktualisierte Ausgabe zu sehen:

```bash
node replaceLast.js
```

Sie sollten jetzt sehen, dass das letzte Vorkommen des Zeichenfolgenmusters in jedem Testfall ersetzt wurde. Beispielsweise sollte "Hello world JavaScript" anstelle von "Hello world world" ausgegeben werden.
