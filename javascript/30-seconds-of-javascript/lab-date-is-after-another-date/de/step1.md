# Wie man in JavaScript überprüft, ob ein Datum nach einem anderen Datum liegt

Um in JavaScript zu überprüfen, ob ein Datum nach einem anderen Datum liegt, kann man den größer als Operator (`>`) verwenden. Hier ist ein Beispielcodeausschnitt, der überprüft, ob ein gegebenes Datum (`dateA`) nach einem anderen Datum (`dateB`) liegt:

```js
const isAfterDate = (dateA, dateB) => dateA > dateB;
```

Um diese Funktion zu verwenden, geben Sie einfach zwei Datumsobjekte ein, wie folgt:

```js
isAfterDate(new Date(2010, 10, 21), new Date(2010, 10, 20)); // true
```

Um das auszuprobieren, können Sie die Konsole/SSH öffnen und `node` eingeben, um zu beginnen, zu programmieren.
