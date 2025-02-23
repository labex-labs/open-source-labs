# Wie man ein Array von Objekten basierend auf einer Eigenschaftsortierung sortiert

Um ein Array von Objekten basierend auf einer Eigenschaftsortierung zu sortieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduce()`, um aus dem `order`-Array ein Objekt zu erstellen, wobei die Werte als Schlüssel und deren ursprünglicher Index als Wert verwendet werden.
3. Verwenden Sie `Array.prototype.sort()`, um das gegebene Array zu sortieren und Elemente zu überspringen, für die `prop` leer ist oder nicht im `order`-Array enthalten ist.

Hier ist ein Beispielcodeausschnitt zum Sortieren eines Arrays von Objekten basierend auf einer Eigenschaftsortierung:

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

Sie können die `orderWith`-Funktion verwenden, um ein Array von Objekten basierend auf einer Eigenschaftsortierung zu sortieren. Beispiel:

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
