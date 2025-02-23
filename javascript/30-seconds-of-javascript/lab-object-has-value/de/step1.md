# Funktion zum Überprüfen, ob ein Objekt einen bestimmten Wert enthält

Um zu überprüfen, ob ein Objekt einen bestimmten Wert enthält, verwenden Sie die folgende Funktion:

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

Um diese Funktion zu verwenden, übergeben Sie als Argumente das Objekt, das Sie durchsuchen möchten, und den Zielwert. Die Funktion gibt `true` zurück, wenn das Objekt den Wert enthält, und `false`, wenn es ihn nicht enthält.

Hier ist ein Beispiel:

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

Um mit der Programmierung zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein.
