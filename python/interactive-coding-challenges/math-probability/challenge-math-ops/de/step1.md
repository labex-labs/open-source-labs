# Mathematische Operationen

## Problem

Erstellen Sie eine Python-Klasse mit einer `insert`-Methode, die es ermöglicht, eine ganze Zahl in eine Liste einzufügen. Die Klasse sollte auch die Berechnung des Maximums, Minimums, Durchschnitts und Modus der Liste in einer Zeitkomplexität von O(1) unterstützen. Die Klasse sollte die folgenden Szenarien behandeln:

- Wenn die Eingabe ungültig ist, sollte sie einen `TypeError` auslösen.
- Wenn die Liste leer ist, sollte sie einen `ValueError` auslösen.
- Wenn es mehrere Modi gibt, kann sie irgendeinen der Modi zurückgeben.

## Anforderungen

Um das obige Problem zu lösen, müssen wir die folgenden Anforderungen beachten:

- Die Eingaben können ungültig sein, daher dürfen wir nicht davon ausgehen, dass die Eingaben gültig sind.
- Der Bereich der Eingaben liegt zwischen 0 und 100 einschließlich.
- Der Durchschnitt sollte als `float` zurückgegeben werden.
- Die anderen Ergebnisse sollten als `integer` zurückgegeben werden.
- Wenn es mehrere Modi gibt, kann die Klasse irgendeinen der Modi zurückgeben.
- Wir können davon ausgehen, dass die Liste in den Arbeitsspeicher passt.

## Beispielgebrauch

Hier sind einige Beispiele für die Verwendung der Klasse:

- `None` -> `TypeError`
- `[]` -> `ValueError`
- `[5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]`
  - `max`: 9
  - `min`: 2
  - `mean`: 4.909090909090909
  - `mode`: 9 oder 2
