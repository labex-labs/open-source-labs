# Anweisungen zum Auswählen von Objekt-Schlüsseln

Um bestimmte Schlüssel-Wert-Paare aus einem Objekt auszuwählen, verwenden Sie die Funktion `pick(obj, arr)`.

- Geben Sie das Objekt als erstes Argument und ein Array von Schlüsseln, die ausgewählt werden sollen, als zweites Argument an.
- Die Funktion gibt ein neues Objekt zurück, das nur die Schlüssel-Wert-Paare enthält, die den angegebenen Schlüsseln entsprechen.

Hier ist ein Beispiel, wie `pick()` verwendet werden kann:

```js
const pick = (obj, arr) =>
  arr.reduce((acc, curr) => (curr in obj && (acc[curr] = obj[curr]), acc), {});

pick({ a: 1, b: "2", c: 3 }, ["a", "c"]); // { 'a': 1, 'c': 3 }
```

Um mit der Code-Praxis zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
