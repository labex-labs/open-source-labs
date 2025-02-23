# Verwendung des logischen Oder für Funktionen

Um mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Der logische Oder (`||`)-Operator kann verwendet werden, um zu überprüfen, ob mindestens eine Funktion für einen gegebenen Argumentensatz `true` zurückgibt. Dazu rufen Sie die beiden Funktionen mit den bereitgestellten `args` auf und wenden Sie den logischen Oder-Operator auf ihre Ergebnisse an.

Hier ist eine Beispielimplementierung der `either`-Funktion:

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

Und hier ist ein Beispiel für die Verwendung der `either`-Funktion mit zwei Funktionen `isEven` und `isPositive`:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

In diesem Beispiel gibt `isPositiveOrEven` für beide `4` und `3` `true` zurück, da `isEven` für `4` `true` zurückgibt und `isPositive` für `3` `true` zurückgibt.
