# Funktion zum Finden umgekehrter eindeutiger Werte in einem Array

Um alle eindeutigen Werte eines Arrays basierend auf einer bereitgestellten Vergleichsfunktion von rechts zu finden, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausführung zu beginnen.
2. Verwenden Sie `Array.prototype.reduceRight()` und `Array.prototype.some()`, um ein Array zu erstellen, das nur das letzte eindeutige Vorkommen jedes Werts enthält, basierend auf der Vergleichsfunktion `fn`.
3. Die Vergleichsfunktion nimmt zwei Argumente entgegen: die Werte der beiden zu vergleichenden Elemente.
4. Hier ist der Code, um die Funktion zu implementieren:

```js
const uniqueElementsByRight = (arr, fn) =>
  arr.reduceRight((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

5. Verwenden Sie den folgenden Code, um die Funktion zu testen:

```js
uniqueElementsByRight(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'e' }, { id: 1, value: 'd' }, { id: 2, value: 'c' } ]
```
