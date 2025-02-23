# Umwandlung von Zeichenketten in CamelCase

Um eine Zeichenkette in CamelCase umzuwandeln, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Verwenden Sie `String.prototype.match()` mit einem geeigneten regulären Ausdruck, um die Zeichenkette in Wörter aufzuteilen.
3. Verwenden Sie `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toLowerCase()` und `String.prototype.toUpperCase()`, um die Wörter zu kombinieren und den ersten Buchstaben jedes Wortes in Großbuchstaben zu setzen.
4. Verwenden Sie die unten gezeigte `toCamelCase`-Funktion, um die Umwandlung durchzuführen:

```js
const toCamelCase = (str) => {
  const words =
    str &&
    str.match(
      /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g
    );
  const capitalizedWords =
    words &&
    words.map(
      (word) => word.slice(0, 1).toUpperCase() + word.slice(1).toLowerCase()
    );
  const camelCaseString = capitalizedWords && capitalizedWords.join("");
  return (
    camelCaseString &&
    camelCaseString.slice(0, 1).toLowerCase() + camelCaseString.slice(1)
  );
};
```

Hier sind einige Beispiele für die Verwendung der `toCamelCase`-Funktion:

```js
toCamelCase("some_database_field_name"); // 'someDatabaseFieldName'
toCamelCase("Some label that needs to be camelized");
// 'someLabelThatNeedsToBeCamelized'
toCamelCase("some-javascript-property"); // 'someJavascriptProperty'
toCamelCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'someMixedStringWithSpacesUnderscoresAndHyphens'
```
