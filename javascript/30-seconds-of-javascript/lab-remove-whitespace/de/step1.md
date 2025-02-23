# Funktion zum Entfernen von Leerzeichen

Um Leerzeichen aus einer Zeichenkette zu entfernen, verwenden Sie die folgende Funktion.

- Verwenden Sie `String.prototype.replace()` mit einem regulären Ausdruck, um alle Vorkommen von Leerzeichen durch eine leere Zeichenkette zu ersetzen.

```js
const removeWhitespace = (str) => str.replace(/\s+/g, "");
```

## Erklärung des regulären Ausdrucks

- `/\s+/g` zerlegt sich wie folgt:
  - `\s`: Matches any whitespace character (spaces, tabs, line breaks)
  - `+`: Matches one or more occurrences of the previous character
  - `/g`: Global flag - matches all occurrences in the string, not just the first one

## Schnelle Regex-Referenz

Häufige Leerzeichenmuster:

- `\s` - matches any whitespace (space, tab, newline)
- `\t` - matches tab characters
- `\n` - matches newline characters
- `\r` - matches carriage returns
- `` (space) - matches only space characters

Beispielsweise:

```js
removeWhitespace("Lorem ipsum.\n Dolor sit amet. ");
// 'Loremipsum.Dolorsitamet.'

// Weitere Beispiele:
removeWhitespace("Hello    World"); // "HelloWorld"
removeWhitespace("Tab\there\nNew line"); // "TabhereNewline"
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
