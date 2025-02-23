# Wie man Arrayelemente gruppiert

Wenn Sie sich an das Programmieren üben möchten, können Sie beginnen, indem Sie das Terminal/SSH öffnen und `node` eingeben. Wenn Sie bereit sind, können Sie die Elemente eines Arrays basierend auf einer angegebenen Funktion gruppieren, indem Sie die folgenden Schritte ausführen:

1. Verwenden Sie `Array.prototype.map()`, um die Werte des Arrays auf eine Funktion oder eine Eigenschaftsname abzubilden.
2. Verwenden Sie `Array.prototype.reduce()`, um ein Objekt zu erstellen, dessen Schlüssel aus den gemappten Ergebnissen erzeugt werden.

Hier ist ein Beispielcodeausschnitt:

```js
const groupBy = (arr, fn) =>
  arr
    .map(typeof fn === "function" ? fn : (val) => val[fn])
    .reduce((acc, val, i) => {
      acc[val] = (acc[val] || []).concat(arr[i]);
      return acc;
    }, {});
```

Um den Code zu testen, können Sie die folgenden Beispiele verwenden:

```js
groupBy([6.1, 4.2, 6.3], Math.floor); // {4: [4.2], 6: [6.1, 6.3]}
groupBy(["one", "two", "three"], "length"); // {3: ['one', 'two'], 5: ['three']}
```

Diese werden Objekte zurückgeben, deren Schlüssel basierend auf der angegebenen Funktion und deren Werte Arrays der ursprünglichen Elemente sind, die der Funktion entsprechen.
