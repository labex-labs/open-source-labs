# Funktion, um zu überprüfen, ob ein Array in einem anderen Array enthalten ist

Um zu beginnen, öffnen Sie das Terminal/SSH und geben Sie `node` ein. Diese Funktion überprüft, ob alle Elemente des ersten Arrays im zweiten Array vorhanden sind, unabhängig von ihrer Reihenfolge.

Hier sind die Schritte, die Sie zu befolgen haben:

1. Verwenden Sie eine `for...of`-Schleife, um über einen aus dem ersten Array erstellten `Set` zu iterieren.
2. Anwenden Sie `Array.prototype.some()`, um zu überprüfen, ob alle eindeutigen Werte im zweiten Array vorhanden sind.
3. Verwenden Sie `Array.prototype.filter()`, um die Anzahl der Vorkommen jedes eindeutigen Werts in beiden Arrays zu vergleichen.
4. Wenn die Anzahl eines Elements im ersten Array größer als im zweiten Array ist, geben Sie `false` zurück. Wenn nicht, geben Sie `true` zurück.

Schauen Sie sich den folgenden Code an, um zu sehen, wie es funktioniert:

```js
const isContainedIn = (a, b) => {
  for (const v of new Set(a)) {
    if (
      !b.some((e) => e === v) ||
      a.filter((e) => e === v).length > b.filter((e) => e === v).length
    )
      return false;
  }
  return true;
};
```

Um die Funktion zu testen, verwenden Sie folgenden Code:

```js
isContainedIn([1, 4], [2, 4, 1]); // true
```
