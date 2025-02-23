# Wie man ein Array in Blöcke einer bestimmten Größe aufteilt

Um zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um ein Array in kleinere Arrays einer bestimmten Größe aufzuteilen, gehen Sie folgenschrittweise vor:

1. Verwenden Sie `Array.from()`, um ein neues Array zu erstellen, das der Anzahl der zu erzeugenden Blöcke entspricht.
2. Verwenden Sie `Array.prototype.slice()`, um jedes Element des neuen Arrays auf einen Block der Länge `size` abzubilden.
3. Wenn das ursprüngliche Array nicht gleichmäßig aufgeteilt werden kann, enthält der letzte Block die verbleibenden Elemente.

Hier ist ein Beispielcodeausschnitt:

```js
const chunk = (arr, size) =>
  Array.from({ length: Math.ceil(arr.length / size) }, (v, i) =>
    arr.slice(i * size, i * size + size)
  );
```

Sie können diese Funktion verwenden, indem Sie das Array, das Sie aufteilen möchten, und die gewünschte Größe der Blöcke übergeben. Beispiel:

```js
chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
```
