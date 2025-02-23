# Kompaktierungsalgorithmus für Objekte

Um alle falschen Werte tiefgehend aus einem Objekt oder einem Array zu entfernen, verwenden Sie folgenden Algorithmus:

1. Verwenden Sie Rekursion, um die `compactObject()`-Funktion auf jedes geschachtelte Objekt oder Array aufzurufen.
2. Initialisieren Sie die iterierbare Daten mithilfe von `Array.isArray()`, `Array.prototype.filter()` und `Boolean()`. Dies wird getan, um spärliche Arrays zu vermeiden.
3. Verwenden Sie `Object.keys()` und `Array.prototype.reduce()`, um über jede Schlüssel mit einem geeigneten Anfangswert zu iterieren.
4. Verwenden Sie `Boolean()`, um die Wahrheit eines jeden Schlüsselwerts zu bestimmen und ihn dem Akkumulator hinzuzufügen, wenn er wahr ist.
5. Verwenden Sie `typeof`, um zu bestimmen, ob ein gegebener Wert ein `object` ist, und rufen Sie die Funktion erneut auf, um es tiefgehend zu kompaktieren.

Hier ist der Code für die `compactObject()`-Funktion:

```js
const compactObject = (val) => {
  const data = Array.isArray(val) ? val.filter(Boolean) : val;
  return Object.keys(data).reduce(
    (acc, key) => {
      const value = data[key];
      if (Boolean(value))
        acc[key] = typeof value === "object" ? compactObject(value) : value;
      return acc;
    },
    Array.isArray(val) ? [] : {}
  );
};
```

Um diese Funktion zu verwenden, übergeben Sie ein Objekt oder ein Array als Argument an `compactObject()`. Die Funktion wird ein neues Objekt oder Array zurückgeben, aus dem alle falschen Werte entfernt wurden.

Beispiel:

```js
const obj = {
  a: null,
  b: false,
  c: true,
  d: 0,
  e: 1,
  f: "",
  g: "a",
  h: [null, false, "", true, 1, "a"],
  i: { j: 0, k: false, l: "a" }
};
compactObject(obj);
// { c: true, e: 1, g: 'a', h: [ true, 1, 'a' ], i: { l: 'a' } }
```
