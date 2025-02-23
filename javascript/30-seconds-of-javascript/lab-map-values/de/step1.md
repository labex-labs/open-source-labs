# Funktion zum Abbilden von Objektwerten

Um die Werte eines Objekts mit einer bereitgestellten Funktion abzubilden und ein neues Objekt mit denselben Schlüsseln zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Object.keys()`, um über die Schlüssel des Objekts zu iterieren.
3. Verwenden Sie `Array.prototype.reduce()`, um ein neues Objekt mit denselben Schlüsseln und abgebildeten Werten mit der bereitgestellten Funktion `fn` zu erstellen.
4. Der folgende Code demonstriert die Implementierung der `mapValues`-Funktion.

```js
const mapValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k] = fn(obj[k], k, obj);
    return acc;
  }, {});
```

Hier ist ein Beispiel für die Verwendung der `mapValues`-Funktion:

```js
const users = {
  fred: { user: "fred", age: 40 },
  pebbles: { user: "pebbles", age: 1 }
};
mapValues(users, (u) => u.age); // { fred: 40, pebbles: 1 }
```
