# Das maximale Datum finden

Um den maximalen Datumswert aus einem gegebenen Array von Daten zu finden, führen Sie die folgenden Schritte aus:

1. Öffnen Sie das Terminal oder SSH.
2. Tippen Sie `node`, um mit der Codeausübung zu beginnen.
3. Verwenden Sie die ES6-Spread-Syntax mit `Math.max()`, um den maximalen Datumswert zu finden.
4. Konvertieren Sie den maximalen Datumswert in ein `Date`-Objekt, indem Sie den `Date`-Konstruktor verwenden.

Hier ist ein Beispielcodeausschnitt:

```js
const maxDate = (...dates) => new Date(Math.max(...dates));

const dates = [
  new Date(2017, 4, 13),
  new Date(2018, 2, 12),
  new Date(2016, 0, 10),
  new Date(2016, 0, 9)
];

maxDate(...dates); // Gibt "2018-03-11T22:00:00.000Z" zurück
```

Indem Sie diese Schritte befolgen und den bereitgestellten Code verwenden, können Sie leicht den maximalen Datumswert aus einem gegebenen Array von Daten finden.
