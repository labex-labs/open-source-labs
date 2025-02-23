# Passende Schlüssel finden

Um alle Schlüssel in einem Objekt zu finden, die einem bestimmten Wert entsprechen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Object.keys()`, um alle Eigenschaften des Objekts abzurufen.
3. Verwenden Sie `Array.prototype.filter()`, um jedes Schlüssel-Wert-Paar zu testen und alle Schlüssel zurückzugeben, die dem angegebenen Wert entsprechen.

Hier ist eine Beispiel-Funktion, die diese Logik implementiert:

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

Sie können diese Funktion wie folgt verwenden:

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
