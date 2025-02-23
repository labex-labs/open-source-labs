# Funktion, um den letzten Schlüssel zu finden, der einer Bedingung entspricht

Um den letzten Schlüssel in einem Objekt zu finden, der einer bestimmten Bedingung entspricht, verwenden Sie die `findLastKey`-Funktion. Diese Funktion nimmt ein Objekt und eine Prüfungsfunktion als Argumente entgegen. Wenn ein passender Schlüssel gefunden wird, gibt die Funktion ihn zurück. Andernfalls gibt sie `undefined` zurück. Hier sind die Schritte, die die Funktion zur Suche nach dem letzten Schlüssel ausführt:

1. Verwenden Sie `Object.keys()`, um alle Eigenschaften des Objekts zu erhalten.
2. Verwenden Sie `Array.prototype.reverse()`, um die Reihenfolge der Schlüssel umzukehren.
3. Verwenden Sie `Array.prototype.find()`, um die bereitgestellte Funktion für jedes Schlüssel-Wert-Paar zu testen. Die Callback-Funktion erhält drei Argumente - den Wert, den Schlüssel und das Objekt.
4. Wenn ein passender Schlüssel gefunden wird, geben Sie ihn zurück.

```js
const findLastKey = (obj, fn) =>
  Object.keys(obj)
    .reverse()
    .find((key) => fn(obj[key], key, obj));
```

Hier ist ein Beispiel für die Verwendung von `findLastKey`:

```js
findLastKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'pebbles'
```

Um diese Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein, um zu beginnen, zu programmieren.
