# Zweitgrößter Knoten in einem BST

## Problemstellung

Gegeben einen binären Suchbaum, finde den zweitgrößten Knoten im Baum. Wenn die Eingabe None oder ein einzelner Knoten ist, sollte eine Ausnahme ausgelöst werden.

Um dieses Problem zu lösen, können wir den Baum in einer bestimmten Reihenfolge durchlaufen und dabei den zweitgrößten Knoten im Auge behalten, den wir bisher gesehen haben. Wir beginnen mit dem Durchlaufen des rechten Teilbaums des Wurzelknotens. Ist der rechte Teilbaum None, so ist der größte Knoten der Wurzelknoten selbst. Ist der rechte Teilbaum nicht None, können wir den rechten Teilbaum fortsetzen durchlaufen, bis wir zu einem Knoten gelangen, der keinen rechten Nachfolger hat. An diesem Punkt ist der größte Knoten im Baum der Elternknoten dieses Knotens. Hat dieser Elternknoten einen linken Nachfolger, so ist der zweitgrößte Knoten der größte Knoten im linken Teilbaum des Elternknotens. Hat der Elternknoten keinen linken Nachfolger, so ist der zweitgrößte Knoten der Elternknoten selbst.

## Anforderungen

Die Anforderungen an diese Herausforderung lauten wie folgt:

- Wenn die Eingabe None oder ein einzelner Knoten ist, sollte eine Ausnahme ausgelöst werden.
  - Eine None-Eingabe sollte einen TypeError auslösen.
  - Eine Eingabe eines einzelnen Knotens sollte einen ValueError auslösen.
- Wir können davon ausgehen, dass wir bereits eine Node-Klasse mit einer insert-Methode haben.
- Wir können davon ausgehen, dass dieses Problem in den verfügbaren Ressourcen lösbar ist.

## Beispielverwendung

Hier sind einige Beispiele, wie diese Funktion verwendet werden kann:

- None oder einzelner Knoten -> Ausnahme

```txt
Eingabe:
                _10_
              _/    \_
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Ausgabe: 20

Eingabe:
                 10
                 /
                5
               / \
              3   7
Ausgabe: 7
```
