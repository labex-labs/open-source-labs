# JavaScript-Funktion zum Großschreiben des ersten Buchstabens eines Strings

Um den ersten Buchstaben eines Strings in JavaScript in Großbuchstaben zu schreiben, verwenden Sie die folgende Funktion:

```js
const capitalize = (str, lowerRest = false) => {
  const [first, ...rest] = str;
  return (
    first.toUpperCase() +
    (lowerRest ? rest.join("").toLowerCase() : rest.join(""))
  );
};
```

Diese Funktion verwendet Array-Destrukturierung und `String.prototype.toUpperCase()`, um den ersten Buchstaben des Strings in Großbuchstaben zu schreiben. Das Argument `lowerRest` ist optional und kann auf `true` gesetzt werden, um den Rest des Strings in Kleinbuchstaben zu konvertieren.

Hier ist ein Beispiel, wie diese Funktion verwendet werden kann:

```js
capitalize("fooBar"); // 'FooBar'
capitalize("fooBar", true); // 'Foobar'
```
