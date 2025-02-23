# Funktion zum Abbilden von Objekt-Schlüsseln

Um die Schlüssel eines Objekts mithilfe einer bereitgestellten Funktion abzubilden und ein neues Objekt zu erzeugen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Code-Praxis zu beginnen.
2. Verwenden Sie `Object.keys()`, um über die Schlüssel des Objekts zu iterieren.
3. Verwenden Sie `Array.prototype.reduce()`, um ein neues Objekt mit denselben Werten und abgebildeten Schlüsseln mithilfe der bereitgestellten Funktion (`fn`) zu erstellen.

Hier ist eine Beispiel-Implementierung der `mapKeys`-Funktion:

```js
const mapKeys = (obj, fn) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[fn(obj[k], k, obj)] = obj[k];
    return acc;
  }, {});
```

Sie können die Funktion mit einem Beispiel-Eingabe wie dieser testen:

```js
mapKeys({ a: 1, b: 2 }, (val, key) => key + val); // { a1: 1, b2: 2 }
```
