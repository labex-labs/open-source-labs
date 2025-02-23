# Wie man überprüft, ob ein Objekt tief eingefroren ist

Um zu überprüfen, ob ein Objekt tief eingefroren ist, folgen Sie diesen Schritten in JavaScript:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie Rekursion, um zu überprüfen, ob alle Eigenschaften des Objekts tief eingefroren sind.
3. Verwenden Sie `Object.isFrozen()` auf dem angegebenen Objekt, um zu überprüfen, ob es oberflächlich eingefroren ist.
4. Verwenden Sie `Object.keys()`, um alle Eigenschaften des Objekts zu erhalten, und `Array.prototype.every()`, um zu überprüfen, dass alle Schlüssel entweder tief eingefrorene Objekte oder nicht-Objektwerte sind.

Hier ist ein Beispielcodeausschnitt, um zu überprüfen, ob ein Objekt tief eingefroren ist:

```js
const isDeepFrozen = (obj) =>
  Object.isFrozen(obj) &&
  Object.keys(obj).every(
    (prop) => typeof obj[prop] !== "object" || isDeepFrozen(obj[prop])
  );
```

Sie können die `isDeepFrozen`-Funktion verwenden, um zu überprüfen, ob ein Objekt tief eingefroren ist, wie folgt:

```js
const x = Object.freeze({ a: 1 });
const y = Object.freeze({ b: { c: 2 } });
isDeepFrozen(x); // true
isDeepFrozen(y); // false
```
