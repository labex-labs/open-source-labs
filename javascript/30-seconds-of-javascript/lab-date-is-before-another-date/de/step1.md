# Wie man in JavaScript überprüft, ob ein Datum vor einem anderen liegt

Um in JavaScript zu überprüfen, ob ein Datum vor einem anderen liegt, kann man den kleiner als Operator (`<`) verwenden. Hier ist eine Beispiel-Funktion, die zwei Datumsangaben entgegennimmt und einen booleschen Wert zurückgibt, der angibt, ob das erste Datum vor dem zweiten liegt:

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

Man kann diese Funktion verwenden, um zu überprüfen, ob ein bestimmtes Datum vor einem anderen Datum liegt, indem man zwei `Date`-Objekte als Argumente übergibt. Beispielsweise:

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
