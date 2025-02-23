# Verwendung des logischen UND mit Funktionen

Um zu beginnen, mit der Programmierung zu üben, öffnen Sie das Terminal/SSH und geben Sie `node` ein.

Um zu überprüfen, ob zwei Funktionen für einen gegebenen Satz von Argumenten `true` zurückgeben, verwenden Sie den logischen UND (`&&`)-Operator.

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

Der obige Code erstellt eine neue Funktion `both`, die zwei Funktionen `f` und `g` als Eingabe nimmt und eine andere Funktion zurückgibt, die `f` und `g` mit den übergebenen Argumenten aufruft und nur dann `true` zurückgibt, wenn beide Funktionen `true` zurückgeben.

Zum Beispiel können wir die `isEven`- und `isPositive`-Funktionen mit `both` verwenden, um zu überprüfen, ob eine Zahl sowohl positiv als auch gerade ist, wie unten gezeigt:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

Hier ist `isPositiveEven` eine neue Funktion, die überprüft, ob eine gegebene Zahl sowohl positiv als auch gerade ist, indem sie die `both`-Funktion mit `isEven` und `isPositive` als Eingaben verwendet.
