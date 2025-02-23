# Wie man in JavaScript die Objektgleichheit überprüft

Um zu überprüfen, ob zwei Werte gleichwertig sind, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Führen Sie einen tiefen Vergleich zwischen den beiden Werten mit der `equals()`-Funktion durch.
3. Überprüfen Sie, ob die beiden Werte identisch sind. Wenn ja, geben Sie `true` zurück.
4. Überprüfen Sie, ob beide Werte `Date`-Objekte mit der gleichen Zeit sind, indem Sie `Date.prototype.getTime()` verwenden. Wenn ja, geben Sie `true` zurück.
5. Überprüfen Sie, ob beide Werte nicht-Objektwerte mit einem gleichwertigen Wert sind (strenger Vergleich). Wenn ja, geben Sie `true` zurück.
6. Überprüfen Sie, ob nur ein Wert `null` oder `undefined` ist oder ob ihre Prototypen unterschiedlich sind. Wenn ja, geben Sie `false` zurück.
7. Wenn keine der obigen Bedingungen zutrifft, verwenden Sie `Object.keys()`, um zu überprüfen, ob beide Werte die gleiche Anzahl von Schlüsseln haben.
8. Verwenden Sie `Array.prototype.every()`, um zu überprüfen, ob jeder Schlüssel in `a` in `b` existiert und ob sie rekursiv durch Aufruf von `equals()` gleichwertig sind.

Verwenden Sie den folgenden Code, um die `equals()`-Funktion zu implementieren:

```js
const equals = (a, b) => {
  if (a === b) return true;

  if (a instanceof Date && b instanceof Date)
    return a.getTime() === b.getTime();

  if (!a || !b || (typeof a !== "object" && typeof b !== "object"))
    return a === b;

  if (a.prototype !== b.prototype) return false;

  const keys = Object.keys(a);
  if (keys.length !== Object.keys(b).length) return false;

  return keys.every((k) => equals(a[k], b[k]));
};
```

Verwenden Sie die folgenden Codebeispiele, um die `equals()`-Funktion zu testen:

```js
equals(
  { a: [2, { e: 3 }], b: [4], c: "foo" },
  { a: [2, { e: 3 }], b: [4], c: "foo" }
); // true

equals([1, 2, 3], { 0: 1, 1: 2, 2: 3 }); // true
```
