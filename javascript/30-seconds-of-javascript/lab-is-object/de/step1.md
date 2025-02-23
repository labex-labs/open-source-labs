# Bestimmen, ob ein Wert ein Objekt ist

Um zu bestimmen, ob ein übergebener Wert ein Objekt ist, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Die folgenden Schritte werden ausgeführt:

- Der `Object`-Konstruktor erstellt einen Objektwrapper für den gegebenen Wert.
- Wenn der Wert `null` oder `undefined` ist, wird ein leeres Objekt erstellt und zurückgegeben.
- Wenn der Wert nicht `null` oder `undefined` ist, wird ein Objekt vom Typ, der dem gegebenen Wert entspricht, zurückgegeben.

Hier ist eine Beispiel-Funktion, die überprüft, ob ein Wert ein Objekt ist:

```js
const isObject = (obj) => obj === Object(obj);
```

Hier sind einige Beispiele für die Verwendung der `isObject`-Funktion:

```js
isObject([1, 2, 3, 4]); // true
isObject([]); // true
isObject(["Hello!"]); // true
isObject({ a: 1 }); // true
isObject({}); // true
isObject(true); // false
```
