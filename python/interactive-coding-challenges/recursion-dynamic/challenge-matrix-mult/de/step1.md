# Matrix Mult

## Problem

Gegeben eine Liste von 2x2 Matrizen müssen wir den minimalen Kosten der Multiplikation dieser Matrizen berechnen. Die Kosten der Multiplikation zweier Matrizen entsprechen der Anzahl der Skalarmultiplikationen, die erforderlich sind. Beispielsweise, wenn wir Matrizen A, B und C haben und das Produkt ABC berechnen möchten, so wären die Kosten die Anzahl der Skalarmultiplikationen, die erforderlich sind, um jedes Element der resultierenden Matrix zu berechnen.

Um dieses Problem zu lösen, müssen wir die optimale Reihenfolge der Matrixmultiplikation finden. Die Reihenfolge, in der wir die Matrizen multiplizieren, hat einen Einfluss auf die Gesamtkosten der Multiplikation. Beispielsweise, wenn wir Matrizen A, B und C haben und das Produkt ABC berechnen möchten, können wir entweder (AB)C oder A(BC) berechnen. Die Kosten dieser beiden Berechnungen können unterschiedlich sein, und wir müssen die optimale Reihenfolge finden, die die Kosten minimiert.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Wir müssen nur die Kosten der Matrixmultiplikation berechnen und nicht die tatsächliche Reihenfolge der Operationen auflisten.
- Wir dürfen nicht annehmen, dass die Eingaben gültig sind und müssen ungültige Eingaben behandeln.
- Wir können annehmen, dass das Problem in den Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verhalten sollte:

- `None` -> `Exception`
- `[]` -> `0`
- `[Matrix(2, 3), Matrix(3, 6), Matrix(6, 4), Matrix(4, 5)]` -> `124`
