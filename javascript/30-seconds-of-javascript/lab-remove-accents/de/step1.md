# Akzente entfernen

Diese Funktion entfernt Akzente aus Zeichenketten.

- Verwenden Sie `String.prototype.normalize()`, um die Zeichenkette in ein normalisiertes Unicode-Format zu konvertieren.
- Verwenden Sie `String.prototype.replace()`, um diakritische Zeichen im angegebenen Unicode-Bereich durch leere Zeichenketten zu ersetzen.

```js
const removeAccents = (str) =>
  str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
```

Um diese Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Rufen Sie dann die Funktion mit einer Zeichenkette als Argument auf.

```js
removeAccents("Antoine de Saint-Exupéry"); // 'Antoine de Saint-Exupery'
```
