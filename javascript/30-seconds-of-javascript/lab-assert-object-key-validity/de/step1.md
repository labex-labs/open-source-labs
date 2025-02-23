# Objekt-Schlüssel validieren

Um sicherzustellen, dass alle Schlüssel in einem Objekt den angegebenen `keys` entsprechen, folgen Sie diesen Schritten:

- Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
- Verwenden Sie `Object.keys()`, um die Schlüssel des Objekts `obj` abzurufen.
- Verwenden Sie `Array.prototype.every()` und `Array.prototype.includes()`, um zu validieren, dass jeder Schlüssel im Objekt im `keys`-Array enthalten ist.

Hier ist eine Beispielimplementierung:

```js
const validateObjectKeys = (obj, keys) =>
  Object.keys(obj).every((key) => keys.includes(key));
```

Sie können die Funktion wie folgt verwenden:

```js
validateObjectKeys({ id: 10, name: "apple" }, ["id", "name"]); // true
validateObjectKeys({ id: 10, name: "apple" }, ["id", "type"]); // false
```
