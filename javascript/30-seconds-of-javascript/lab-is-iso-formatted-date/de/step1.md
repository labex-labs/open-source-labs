# Überprüfen, ob eine Zeichenkette im ISO-Format vorliegt

Um zu überprüfen, ob eine gegebene Zeichenkette (string) im vereinfachten erweiterten ISO-Format (ISO 8601) vorliegt, befolgen Sie diese Schritte:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
2. Verwenden Sie den `Date`-Konstruktor, um aus der gegebenen Zeichenkette ein `Date`-Objekt zu erstellen.
3. Überprüfen Sie, ob das erstellte Datumsobjekt gültig ist, indem Sie `Date.prototype.valueOf()` und `Number.isNaN()` verwenden.
4. Vergleichen Sie die ISO-formatierte Zeichenkettenrepräsentation des Datums mit der ursprünglichen Zeichenkette mithilfe von `Date.prototype.toISOString()`.
5. Wenn die Zeichenketten übereinstimmen und das Datum gültig ist, geben Sie `true` zurück. Andernfalls geben Sie `false` zurück.

Hier ist ein Beispiel-Codeausschnitt:

```js
const isISOString = (val) => {
  const d = new Date(val);
  return !Number.isNaN(d.valueOf()) && d.toISOString() === val;
};

isISOString("2020-10-12T10:10:10.000Z"); // true
isISOString("2020-10-12"); // false
```

Diese Funktion gibt `true` zurück, wenn die Zeichenkette im ISO-Format vorliegt, und `false` sonst.
