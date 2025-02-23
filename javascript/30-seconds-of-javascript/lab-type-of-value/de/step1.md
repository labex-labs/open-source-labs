# Funktion zum Abrufen des Typs eines Werts

Um den Typ eines Werts abzurufen, verwenden Sie die folgende Funktion:

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- Die Funktion gibt `'undefined'` oder `'null'` zurück, wenn der Wert `undefined` oder `null` ist.
- Andernfalls gibt sie den Namen des Konstruktors zurück, indem sie `Object.prototype.constructor` und `Function.prototype.name` verwendet.

Beispielverwendung:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
