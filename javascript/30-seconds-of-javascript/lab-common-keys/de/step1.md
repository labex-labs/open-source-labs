# Tipps für das Programmieren und das Finden von gemeinsamen Schlüsseln

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um die gemeinsamen Schlüssel zwischen zwei Objekten zu finden, folgen Sie diesen Schritten:

1. Verwenden Sie `Object.keys()`, um die Schlüssel des ersten Objekts zu erhalten.
2. Verwenden Sie `Object.prototype.hasOwnProperty()`, um zu überprüfen, ob das zweite Objekt einen Schlüssel hat, der im ersten Objekt vorhanden ist.
3. Verwenden Sie `Array.prototype.filter()`, um Schlüssel zu filtern, die in beiden Objekten nicht vorhanden sind.

Hier ist ein Beispiel für den Code:

```js
const commonKeys = (obj1, obj2) =>
  Object.keys(obj1).filter((key) => obj2.hasOwnProperty(key));
```

Sie können den Code mit diesem Beispiel testen:

```js
commonKeys({ a: 1, b: 2 }, { a: 2, c: 1 }); // ['a']
```
