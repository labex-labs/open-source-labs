# Wie man die Schlüssel eines Objekts in JavaScript in Großbuchstaben umwandelt

Um alle Schlüssel eines Objekts in JavaScript in Großbuchstaben umzuwandeln, befolgen Sie diese Schritte:

1. Verwenden Sie `Object.keys()`, um ein Array der Schlüssel des Objekts zu erhalten.
2. Verwenden Sie `Array.prototype.reduce()`, um das Array auf ein Objekt abzubilden.
3. Verwenden Sie `String.prototype.toUpperCase()`, um die Schlüssel in Großbuchstaben umzuwandeln.

Hier ist der Code:

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

Um die Funktion zu testen, können Sie sie wie folgt aufrufen:

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
