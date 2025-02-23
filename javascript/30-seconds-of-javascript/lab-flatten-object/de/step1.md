# Ein Objekt flachstellen

Um ein Objekt mit Pfaden für die Schlüssel zu flachstellen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um das Objekt zu flachstellen.
3. Verwenden Sie `Object.keys()`, kombiniert mit `Array.prototype.reduce()`, um jeden Blattknoten in einen flachen Pfadknoten umzuwandeln.
4. Wenn der Wert eines Schlüssels ein Objekt ist, rufen Sie die Funktion rekursiv mit dem entsprechenden `prefix` auf, um den Pfad mit `Object.assign()` zu erstellen.
5. Andernfalls fügen Sie das entsprechend vorangestellte Schlüssel-Wert-Paar dem Akkumulatorobjekt hinzu.
6. Überspringen Sie das zweite Argument, `prefix`, es sei denn, Sie möchten, dass jeder Schlüssel einen Präfix hat.

Hier ist eine Beispielimplementierung:

```js
const flattenObject = (obj, prefix = "") =>
  Object.keys(obj).reduce((acc, k) => {
    const pre = prefix.length ? `${prefix}.` : "";
    if (
      typeof obj[k] === "object" &&
      obj[k] !== null &&
      Object.keys(obj[k]).length > 0
    ) {
      Object.assign(acc, flattenObject(obj[k], pre + k));
    } else {
      acc[pre + k] = obj[k];
    }
    return acc;
  }, {});
```

Sie können die `flattenObject`-Funktion wie folgt verwenden:

```js
flattenObject({ a: { b: { c: 1 } }, d: 1 }); // { 'a.b.c': 1, d: 1 }
```
