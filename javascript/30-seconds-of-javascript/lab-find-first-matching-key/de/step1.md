# Funktion, um den ersten Schlüssel zu finden, der einer Prüfung entspricht

Um den ersten Schlüssel in einem Objekt zu finden, der einer gegebenen Testfunktion entspricht, verwenden Sie die `findKey()`-Funktion. Zunächst erhalten Sie alle Objekteigenschaften mit `Object.keys()`. Anschließend wenden Sie die Testfunktion auf jedes Schlüssel-Wert-Paar an, indem Sie `Array.prototype.find()` verwenden. Die Testfunktion sollte drei Argumente entgegennehmen: den Wert, den Schlüssel und das Objekt. Die Funktion gibt den ersten Schlüssel zurück, der der Testfunktion entspricht, oder `undefined`, wenn keiner gefunden wird.

Hier ist eine Beispielimplementierung von `findKey()`:

```js
const findKey = (obj, fn) =>
  Object.keys(obj).find((key) => fn(obj[key], key, obj));
```

Um `findKey()` zu verwenden, übergeben Sie das Objekt und die Testfunktion als Argumente:

```js
findKey(
  {
    barney: { age: 36, active: true },
    fred: { age: 40, active: false },
    pebbles: { age: 1, active: true }
  },
  (x) => x["active"]
); // 'barney'
```

In diesem Beispiel gibt `findKey()` den ersten Schlüssel im Objekt zurück, bei dem der Wert der `active`-Eigenschaft `true` ist, nämlich `'barney'`.
