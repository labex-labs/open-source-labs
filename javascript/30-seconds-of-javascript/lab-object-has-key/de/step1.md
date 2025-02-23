# JavaScript-Funktion zum Überprüfen, ob ein Objekt einen Schlüssel hat

Um zu überprüfen, ob ein Zielwert in einem JavaScript-Objekt vorhanden ist, verwenden Sie die `hasKey`-Funktion.

Die Funktion nimmt zwei Argumente entgegen: `obj`, das JSON-Objekt, in dem gesucht werden soll, und `keys`, ein Array von Schlüsseln, die überprüft werden sollen. Hier sind die Schritte, um zu überprüfen, ob das Objekt den angegebenen Schlüssel hat:

1. Überprüfen Sie, ob das `keys`-Array nicht leer ist. Wenn es leer ist, geben Sie `false` zurück.
2. Verwenden Sie die `Array.prototype.every()`-Methode, um über das `keys`-Array zu iterieren und jeden Schlüssel sequentiell bis zur internen Tiefe von `obj` zu überprüfen.
3. Verwenden Sie die `Object.prototype.hasOwnProperty()`-Methode, um zu überprüfen, ob `obj` den aktuellen Schlüssel nicht hat oder kein Objekt ist. Wenn einer dieser Bedingungen zutrifft, stoppen Sie die Ausbreitung und geben Sie `false` zurück.
4. Andernfalls weisen Sie den Wert des Schlüssels `obj` zu, um ihn in der nächsten Iteration zu verwenden.
5. Wenn das `keys`-Array erfolgreich durchlaufen wurde, geben Sie `true` zurück.

Hier ist der Code für die `hasKey`-Funktion:

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

Hier sind einige Beispiele für die Verwendung der `hasKey`-Funktion:

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
