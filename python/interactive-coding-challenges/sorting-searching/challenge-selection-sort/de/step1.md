# Selectionsort

## Problem

Implementieren Sie den Selectionsort in Python. Der Algorithmus sollte eine Liste von ganzen Zahlen als Eingabe entgegennehmen und die sortierte Liste zurückgeben. Der Algorithmus sollte wie folgt funktionieren:

1. Finden Sie das kleinste Element im unsortierten Teil der Liste.
2. Tauschen Sie es mit dem ersten Element des unsortierten Teils der Liste.
3. Verschieben Sie die Grenze des sortierten Teils der Liste um ein Element nach rechts.

Wiederholen Sie die Schritte 1-3, bis die gesamte Liste sortiert ist.

## Anforderungen

Um den Selectionsort in Python zu implementieren, müssen die folgenden Anforderungen erfüllt werden:

- Der Algorithmus sollte eine Liste von ganzen Zahlen als Eingabe entgegennehmen.
- Der Algorithmus sollte eine sortierte Liste von ganzen Zahlen zurückgeben.
- Der Algorithmus sollte mit dem Selectionsort-Algorithmus implementiert werden.
- Der Algorithmus sollte für Listen beliebiger Länge funktionieren.
- Der Algorithmus sollte doppelte Elemente in der Liste behandeln.
- Die Eingabeliste darf nicht sortiert sein.
- Die Eingabeliste kann ungültige Daten enthalten, wie z. B. nicht ganzzahlige Werte.
- Der Algorithmus sollte speicherplatzeffizient sein und nicht zu viel Speicher verwenden.

## Beispielverwendung

Die folgenden Beispiele demonstrieren die Verwendung des Selectionsort-Algorithmus:

- `selection_sort([])` gibt `[]` zurück
- `selection_sort([1])` gibt `[1]` zurück
- `selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])` gibt `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]` zurück
