# Wie man in JavaScript einzigartige Werte in einem Array findet

Um alle einzigartigen Werte in einem Array zu finden, können Sie in JavaScript die folgenden Schritte ausführen:

1. Erstellen Sie aus dem gegebenen Array ein `Set`, um doppelte Werte zu entfernen.
2. Verwenden Sie den Spreadoperator (`...`), um das `Set` wieder in ein Array zu konvertieren.

Hier ist ein Beispielcodeausschnitt:

```js
const getUniqueValues = (arr) => [...new Set(arr)];
```

Sie können die Funktion aufrufen und ihr ein Array übergeben, wie folgt:

```js
getUniqueValues([1, 2, 2, 3, 4, 4, 5]); // [1, 2, 3, 4, 5]
```

Dies wird ein Array zurückgeben, das alle einzigartigen Werte aus dem ursprünglichen Array enthält, ohne jegliche Duplikate.
