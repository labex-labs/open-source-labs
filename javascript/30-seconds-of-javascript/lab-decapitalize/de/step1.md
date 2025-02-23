# Javascript-Funktion zum Ent-Kapitalisieren eines Strings

Um den ersten Buchstaben eines Strings in Kleinbuchstaben zu verwandeln, verwenden Sie die folgende JavaScript-Funktion:

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

Um diese Funktion zu verwenden, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Rufen Sie dann die `decapitalize`-Funktion auf und übergeben Sie als erstes Argument den String, den Sie in Kleinbuchstaben umwandeln möchten.

Optional können Sie das zweite Argument `upperRest` auf `true` setzen, um den Rest des Strings in Großbuchstaben zu konvertieren. Wenn `upperRest` nicht angegeben wird, ist der Standardwert `false`.

Hier sind einige Beispiele:

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
