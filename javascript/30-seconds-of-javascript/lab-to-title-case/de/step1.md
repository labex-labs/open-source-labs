# Funktion zum Konvertieren eines Strings in den Titelfall

Um einen gegebenen String in den Titelfall zu konvertieren, verwenden Sie die folgende Funktion. Sie verwendet `String.prototype.match()`, um den String mit einem geeigneten regulären Ausdruck in Wörter aufzuteilen. Anschließend kombiniert sie sie mit `Array.prototype.map()`, `Array.prototype.slice()`, `Array.prototype.join()` und `String.prototype.toUpperCase()`. Dadurch wird der erste Buchstabe jedes Wortes großgeschrieben und ein Leerzeichen dazwischen hinzugefügt.

```js
const toTitleCase = (str) =>
  str
    .match(/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
```

Hier sind einige Beispiele für die Verwendung der Funktion:

```js
toTitleCase("some_database_field_name"); // 'Some Database Field Name'
toTitleCase("Some label that needs to be title-cased");
// 'Some Label That Needs To Be Title Cased'
toTitleCase("some-package-name"); // 'Some Package Name'
toTitleCase("some-mixed_string with spaces_underscores-and-hyphens");
// 'Some Mixed String With Spaces Underscores And Hyphens'
```
