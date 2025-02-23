# Funktion zum Konvertieren eines Strings in einen URL-Slug

Um einen String in einen Slug umzuwandeln, der in einer URL verwendet werden kann, folge diesen Schritten:

1. Öffne das Terminal/SSH und tippe `node`, um mit der Codeausführung zu beginnen.
2. Verwende die Methoden `String.prototype.toLowerCase()` und `String.prototype.trim()`, um den String zu normalisieren.
3. Verwende die Methode `String.prototype.replace()`, um Leerzeichen, Bindestriche und Unterstriche durch `-` zu ersetzen und Sonderzeichen zu entfernen.
4. Implementiere folgenden Code:

```js
const slugify = (str) =>
  str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_-]+/g, "-")
    .replace(/^-+|-+$/g, "");
```

5. Teste die Funktion mit der Eingabe `slugify('Hello World!');` und es sollte die Ausgabe `'hello-world'` zurückgeben.
