# Funktion zum Ermitteln der Größe von Array, Objekt oder String

Um diese Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion ermittelt die Größe eines Arrays, eines Objekts oder eines Strings.

Um sie zu verwenden:

- Bestimmen Sie den Typ von `val` (`array`, `object` oder `string`).
- Verwenden Sie die `Array.prototype.length`-Eigenschaft für Arrays.
- Verwenden Sie den `length`- oder `size`-Wert, sofern verfügbar, oder die Anzahl der Schlüssel für Objekte.
- Für Strings verwenden Sie die `size` eines von `val` erstellten [`Blob`-Objekts](https://developer.mozilla.org/en-US/docs/Web/API/Blob).

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

Beispiele:

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
