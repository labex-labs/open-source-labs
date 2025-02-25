# Graphenpfad existiert

## Problem

Gegeben ein gerichteter Graph und zwei Knoten, schreiben Sie eine Python-Funktion, um zu bestimmen, ob es einen Pfad zwischen den beiden Knoten gibt.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Annahmen machen:

- Der Graph ist gerichtet.
- Wir haben bereits die Klassen Graph und Node.
- Der Graph ist zusammenhängend.
- Die Eingaben sind gültig.
- Die Lösung passt in den Speicher.

## Beispielverwendung

Angenommen, wir haben folgenden Graphen:

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 1, 6)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 8)
```

Wir können die folgende Funktion verwenden, um zu bestimmen, ob es einen Pfad zwischen zwei Knoten gibt:

```
search_path(start=0, end=2) -> True
search_path(start=0, end=0) -> True
search_path(start=4, end=5) -> False
```

Die ersten beiden Funktionsaufrufe geben True zurück, da es einen Pfad zwischen den Start- und Endknoten gibt. Der letzte Funktionsaufruf gibt False zurück, da es keinen Pfad zwischen den Start- und Endknoten gibt.
