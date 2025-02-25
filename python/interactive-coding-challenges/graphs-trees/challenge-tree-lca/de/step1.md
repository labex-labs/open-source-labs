# Baum LCA

## Problem

Gegeben ist ein Binärbaum und zwei Knoten. Finde ihren niedrigsten gemeinsamen Vorfahren.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Der gegebene Baum ist ein Binärbaum, kein Binärsuchebaum.
- Wir dürfen nicht annehmen, dass die beiden Knoten bereits im Baum sind.
- Wir können annehmen, dass der Binärbaum in den Arbeitsspeicher passt.

## Beispielverwendung

Betrachte den folgenden Binärbaum:

```txt
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
```

Wir können unsere Funktion mit den folgenden Eingaben und erwarteten Ausgaben testen:

- 0, 5 -> None (beide Knoten sind nicht im Baum)
- 5, 0 -> None (beide Knoten sind nicht im Baum)
- 1, 8 -> 3
- 12, 8 -> 5
- 12, 40 -> 10
- 9, 20 -> 9
- 3, 5 -> 5
