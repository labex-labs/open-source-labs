# Wie man in JavaScript eine Zufällige Ganzzahl in einem bestimmten Bereich generiert

Um in JavaScript eine Zufällige Ganzzahl in einem bestimmten Bereich zu generieren, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH und geben Sie `node` ein, um mit der Codeausübung zu beginnen.
2. Verwenden Sie die Methode `Math.random()`, um eine Zufallszahl zwischen 0 und 1 zu generieren.
3. Multiplizieren Sie die Zufallszahl mit der Differenz zwischen dem Maximum und Minimum des Bereichs und addieren Sie dann den Mindestwert zum Ergebnis, um die Zufallszahl auf den gewünschten Bereich abzubilden.
4. Verwenden Sie die Methode `Math.floor()`, um das Ergebnis auf die nächstkleinere Ganzzahl abzurunden.

Hier ist ein Beispielcodeausschnitt, der die obigen Schritte implementiert:

```js
const randomIntegerInRange = (min, max) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
```

Anschließend können Sie die Funktion `randomIntegerInRange()` mit den gewünschten Mindest- und Maximalwerten aufrufen, um eine Zufällige Ganzzahl in diesem Bereich zu generieren. Beispielsweise:

```js
randomIntegerInRange(0, 5); // 2
```
