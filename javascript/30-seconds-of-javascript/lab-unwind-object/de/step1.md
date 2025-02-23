# Objekt unwind-Funktion

Um ein Objekt anhand seiner array-wertigen Eigenschaft aufzulösen, verwenden Sie die `unwind`-Funktion.

- Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
- Die Funktion verwendet Objekt-Destrukturierung, um das Schlüssel-Wert-Paar für den angegebenen `Schlüssel` aus dem Objekt auszuschließen.
- Anschließend verwendet es `Array.prototype.map()` für die Werte des angegebenen `Schlüssels`, um ein Array von Objekten zu erstellen.
- Jedes Objekt enthält die Werte des ursprünglichen Objekts, mit Ausnahme von `key`, der auf seine einzelnen Werte abgebildet wird.

```js
const unwind = (key, obj) => {
  const { [key]: _, ...rest } = obj;
  return obj[key].map((val) => ({ ...rest, [key]: val }));
};
```

Beispielverwendung:

```js
unwind("b", { a: true, b: [1, 2] }); // [{ a: true, b: 1 }, { a: true, b: 2 }]
```
