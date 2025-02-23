# Wie man mit Array.prototype.filter() einen kompakten Array erstellt

Um in JavaScript einen kompakten Array zu erstellen, kannst du die `Array.prototype.filter()`-Methode verwenden, um alle falschen Werte aus dem Array zu entfernen. Falsche Werte umfassen `false`, `null`, `0`, `""`, `undefined` und `NaN`.

Hier ist ein Beispielcodeausschnitt, der zeigt, wie man einen kompakten Array mit `Array.prototype.filter()` erstellt:

```js
const compact = (arr) => arr.filter(Boolean);
```

Dann kannst du die `compact`-Funktion verwenden, um einen kompakten Array zu erstellen, indem du ein Array als Argument übergibst. Beispielsweise:

```js
compact([0, 1, false, 2, "", 3, "a", "e" * 23, NaN, "s", 34]);
// Ausgabe: [ 1, 2, 3, 'a','s', 34 ]
```

Indem du `Array.prototype.filter()` auf diese Weise verwendest, kannst du leicht einen kompakten Array erstellen, der nur wahre Werte enthält.
