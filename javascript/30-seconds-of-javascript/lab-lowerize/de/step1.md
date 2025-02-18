# Umwandeln von Objekt-Schlüsseln in Kleinbuchstaben

Um alle Schlüssel (keys) eines Objekts in Kleinbuchstaben umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH, um mit der Programmierung zu beginnen, und geben Sie `node` ein.
2. Verwenden Sie `Object.keys()`, um ein Array der Schlüssel des Objekts zu erhalten.
3. Verwenden Sie `Array.prototype.reduce()`, um das Array auf ein Objekt abzubilden.
4. Verwenden Sie `String.prototype.toLowerCase()`, um die Schlüssel in Kleinbuchstaben umzuwandeln.

Hier ist ein Beispielcode, der diese Schritte implementiert:

```js
const lowerize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toLowerCase()] = obj[k];
    return acc;
  }, {});
```

Sie können dann die Funktion `lowerize()` mit einem Objekt als Argument aufrufen, um ein neues Objekt mit allen Schlüsseln in Kleinbuchstaben zu erhalten. Beispielsweise:

```js
lowerize({ Name: "John", Age: 22 }); // { name: 'John', age: 22 }
```
