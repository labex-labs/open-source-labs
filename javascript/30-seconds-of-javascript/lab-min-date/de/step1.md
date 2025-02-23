# Wie man das früheste Datum in JavaScript findet

Um den kleinsten Datumswert in JavaScript zu finden, kannst du die ES6-Spread-Syntax mit `Math.min()` und dem `Date`-Konstruktor verwenden. Hier ist ein Beispielcodeausschnitt:

```js
const minDate = (...dates) => new Date(Math.min(...dates));
```

Um diese Funktion zu verwenden, erstelle ein Array von `Date`-Objekten und übergebe es an `minDate()` mit der Spread-Syntax. Hier ist ein Beispiel:

```js
const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];
minDate(...dates); // Gibt ein `Date`-Objekt zurück, das 2016-01-08T22:00:00.000Z repräsentiert
```

Mit diesem Code kannst du leicht den kleinsten Datumswert in JavaScript finden.
