# Erstellen eines gefrorenen Set-Objekts in JavaScript

Um in JavaScript ein gefrorenes `Set`-Objekt zu erstellen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie den `Set`-Konstruktor, um ein neues `Set`-Objekt aus einem `iterable` zu erstellen.
3. Setzen Sie die `add`, `delete` und `clear`-Methoden des neu erstellten Objekts auf `undefined`, um das Objekt effektiv zu sperren.

Hier ist ein Beispielcodeausschnitt:

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Ausgabe: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

Dieser Code erstellt ein gefrorenes `Set`-Objekt aus einem iterierbaren von Zahlen und gibt das Objekt zurück, dessen `add`, `delete` und `clear`-Methoden auf `undefined` gesetzt sind.
