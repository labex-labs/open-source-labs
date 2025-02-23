# Anweisungen zum Extrahieren von Werten aus einem Array von Objekten

Um Werte aus einem Array von Objekten zu extrahieren, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Array.prototype.map()`, um das Array von Objekten auf den Wert eines angegebenen `Schlüssels` für jedes Objekt abzubilden.
3. Implementieren Sie die folgende Funktion:

```js
const pluck = (arr, key) => arr.map((i) => i[key]);
```

4. Testen Sie die Funktion mit einem Beispiel-Array von Objekten:

```js
const simpsons = [
  { name: "lisa", age: 8 },
  { name: "homer", age: 36 },
  { name: "marge", age: 34 },
  { name: "bart", age: 10 }
];
pluck(simpsons, "age"); // [8, 36, 34, 10]
```

Dies wird ein Array von Werten zurückgeben, die dem angegebenen `Schlüssel` aus dem Array von Objekten entsprechen.
