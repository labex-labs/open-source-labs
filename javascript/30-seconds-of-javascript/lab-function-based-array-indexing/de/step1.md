# Funktion zum Indizieren eines Arrays

Um ein Array mithilfe einer Funktion zu indizieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, um aus dem Array ein Objekt zu erstellen.
3. Wenden Sie die bereitgestellte Funktion auf jedes Element des Arrays an, um einen Schlüssel zu erzeugen, und fügen Sie das Schlüssel-Wert-Paar zum Objekt hinzu.

Hier ist ein Beispielcodeausschnitt:

```js
const indexBy = (arr, fn) =>
  arr.reduce((obj, v, i) => {
    obj[fn(v, i, arr)] = v;
    return obj;
  }, {});
```

Sie können diese Funktion wie folgt verwenden:

```js
indexBy(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  (x) => x.id
);
// { '10': { id: 10, name: 'apple' }, '20': { id: 20, name: 'orange' } }
```

Diese Funktion erstellt aus einem Array ein Objekt, indem jedes Element mithilfe einer bereitgestellten Funktion einem Schlüssel zugeordnet wird. Das resultierende Objekt enthält Schlüssel-Wert-Paare, wobei die Schlüssel von der Funktion erzeugt werden und die Werte die ursprünglichen Arrayelemente sind.
