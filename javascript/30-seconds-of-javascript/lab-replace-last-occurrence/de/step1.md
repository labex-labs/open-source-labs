# Das Problem verstehen und die Umgebung einrichten

Bevor wir mit dem Codieren beginnen, verstehen wir zunächst, was unsere `replaceLast`-Funktion tun sollte:

1. Drei Parameter akzeptieren:
   - `str`: Der Eingabe-String, der modifiziert werden soll
   - `pattern`: Das Teilzeichenfolgenmuster oder der reguläre Ausdruck (Regular Expression), nach dem gesucht werden soll
   - `replacement`: Die Zeichenfolge, mit der das letzte Vorkommen ersetzt werden soll

2. Einen neuen String zurückgeben, in dem das letzte Vorkommen des Musters ersetzt wurde.

Erstellen wir jetzt eine JavaScript-Datei, um unsere Funktion zu implementieren:

1. Navigieren Sie im Dateiexplorer des WebIDE in das Projektverzeichnis.
2. Erstellen Sie eine neue Datei mit dem Namen `replaceLast.js` im Verzeichnis `replace-last`.
3. Fügen Sie der Datei die folgende Grundstruktur hinzu:

```javascript
// Function to replace the last occurrence of a pattern in a string
function replaceLast(str, pattern, replacement) {
  // Our implementation will go here
  return str;
}

// We will add test cases here later
```

Um sicherzustellen, dass alles korrekt eingerichtet ist, fügen wir einen einfachen Test hinzu:

```javascript
// Example usage
console.log(replaceLast("Hello world world", "world", "JavaScript"));
```

Jetzt lassen wir unseren Code laufen, um die aktuelle Ausgabe zu sehen:

1. Öffnen Sie das Terminal im WebIDE.
2. Navigieren Sie in das Verzeichnis `replace-last`:
   ```bash
   cd ~/project/replace-last
   ```
3. Führen Sie die JavaScript-Datei mit Node.js aus:
   ```bash
   node replaceLast.js
   ```

Sie sollten `Hello world world` in der Ausgabe sehen, da unsere Funktion derzeit einfach nur den ursprünglichen String zurückgibt, ohne Änderungen vorzunehmen.
