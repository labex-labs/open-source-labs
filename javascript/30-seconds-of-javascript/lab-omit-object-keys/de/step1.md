# Schlüssel aus Objekt entfernen

Um bestimmte Schlüssel aus einem Objekt zu entfernen, verwenden Sie die `omit`-Funktion, die ein Objekt und ein Array von Schlüsseln zum Entfernen akzeptiert.

- Die `Object.keys()`-Methode wird verwendet, um alle Schlüssel des Objekts zu erhalten.
- Die `Array.prototype.filter()`-Methode wird dann verwendet, um die angegebenen Schlüssel aus der Liste der Schlüssel zu entfernen.
- Schließlich wird `Array.prototype.reduce()` verwendet, um ein neues Objekt mit den verbleibenden Schlüssel-Wert-Paaren zu erstellen.

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

Beispielverwendung:

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
