# Anleitung zur Berechnung des Mittelpunkts zwischen zwei Paaren von (x,y)-Punkten:

Um den Mittelpunkt zwischen zwei Paaren von (x,y)-Punkten zu berechnen, folgen Sie diesen Schritten:

1. Spalten Sie das Array auf, um `x1`, `y1`, `x2` und `y2` zu erhalten.
2. Berechnen Sie den Mittelpunkt für jede Dimension, indem Sie die Summe der beiden Endpunkte durch `2` teilen.

Hier ist ein Beispielcodeausschnitt, der die Mittelpunktsberechnung-Funktion implementiert:

```js
const midpoint = ([x1, y1], [x2, y2]) => [(x1 + x2) / 2, (y1 + y2) / 2];
```

Sie können die `midpoint`-Funktion mit den folgenden Parametern aufrufen, um die Mittelpunktkoordinaten zu erhalten:

```js
midpoint([2, 2], [4, 4]); // [3, 3]
midpoint([4, 4], [6, 6]); // [5, 5]
midpoint([1, 3], [2, 4]); // [1.5, 3.5]
```

# Einstieg in die Programmierung:

Um mit der Programmierung zu beginnen, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal/SSH.
2. Geben Sie `node` ein, um die Node.js-Umgebung zu starten.
