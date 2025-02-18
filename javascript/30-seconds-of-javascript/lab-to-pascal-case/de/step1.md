# Funktion zur Umwandlung eines Strings in Pascal Case

Um einen String in Pascal Case umzuwandeln, können Sie die Funktion `toPascalCase()` verwenden. So geht's:

- Öffnen Sie zunächst das Terminal/SSH und geben Sie `node` ein, um mit der Programmierung zu beginnen.
- Verwenden Sie dann die Methode `String.prototype.match()` mit einem geeigneten regulären Ausdruck, um den String in Wörter aufzuteilen.
- Verwenden Sie als Nächstes die Methoden `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()`, `String.prototype.toUpperCase()` und `String.prototype.toLowerCase()`, um die Wörter zusammenzufügen, wobei der erste Buchstabe jedes Wortes großgeschrieben und der Rest klein geschrieben wird.
- Rufen Sie schließlich die Funktion `toPascalCase()` mit Ihrem gewünschten String als Argument auf, um ihn in Pascal Case umzuwandeln.

Hier ist der Code für die Funktion `toPascalCase()`:

```js
const toPascalCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((x) => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase())
    .join("");
```

Sie können diese Funktion verwenden, um jeden String in Pascal Case umzuwandeln. Hier sind einige Beispiele:

```js
toPascalCase("some_database_field_name"); // 'SomeDatabaseFieldName'
toPascalCase("Some label that needs to be pascalized"); // 'SomeLabelThatNeedsToBePascalized'
toPascalCase("some-javascript-property"); // 'SomeJavascriptProperty'
toPascalCase("some-mixed_string with spaces_underscores-and-hyphens"); // 'SomeMixedStringWithSpacesUnderscoresAndHyphens'
```
