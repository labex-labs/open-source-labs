# Graph Build Order

## Problem

Gegeben eine Liste von Projekten und ihren Abhängigkeiten müssen wir eine gültige Build-Order finden. Eine Build-Order ist eine Liste von Projekten, in der jedes Projekt vor jedem Projekt erscheint, auf das es angewiesen ist.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die Eingabe kann einen zyklischen Graphen enthalten.
- Wir können davon ausgehen, dass wir bereits Klassen `Graph` und `Node` haben.
- Wir können davon ausgehen, dass der Graph zusammenhängend ist.
- Wir können davon ausgehen, dass die Eingaben gültig sind.
- Wir können davon ausgehen, dass das Problem in den verfügbaren Speicher passt.

## Beispiel

Angenommen, wir haben die folgenden Projekte und Abhängigkeiten:

- Projekte: a, b, c, d, e, f, g
- Abhängigkeiten: (d, g), (f, c), (f, b), (f, a), (c, a), (b, a), (a, e), (b, e)

Die Ausgabe sollte dann: d, f, c, b, g, a, e sein.

Beachten Sie, dass die Kantenrichtung nach unten zeigt, was bedeutet, dass ein Projekt von den Projekten abhängt, die darunter stehen.

```txt
    f     d
   /|\    |
  c | b   g
   \|/|
    a |
    |/
    e
```

Wenn die Eingabe einen zyklischen Graphen enthält, sollte die Ausgabe `None` sein.
