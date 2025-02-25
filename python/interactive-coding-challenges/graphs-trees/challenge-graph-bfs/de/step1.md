# Graph Bfs

## Problem

Das Implementieren des Breitensuche-Algorithmus (BFS) für einen Graphen besteht darin, alle Knoten des Graphen in breitfirstiger Reihenfolge zu besuchen, beginnend von einem angegebenen Startknoten. Der Algorithmus funktioniert, indem er zunächst den Startknoten besucht, dann alle seine Nachbarn, dann alle Nachbarn seiner Nachbarn usw. Der Reihenfolge, in der die Knoten besucht werden, kommt es dabei sehr darauf an, da sie den kürzesten Pfad vom Startknoten zu allen anderen Knoten im Graphen bestimmt.

## Anforderungen

Um den BFS für einen Graphen zu implementieren, müssen die folgenden Anforderungen erfüllt sein:

- Der Graph ist gerichtet.
- Die Klassen Graph und Node sind bereits verfügbar.
- Der Graph ist zusammenhängend.
- Die Eingaben sind gültig.
- Der Algorithmus passt in den Speicher.

## Beispielverwendung

Angenommen, wir haben einen Graphen mit folgenden Kanten:

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

Wenn wir den BFS von Knoten 0 starten, wird die Reihenfolge der besuchten Knoten [0, 1, 4, 5, 3, 2] sein. Dies bedeutet, dass zuerst Knoten 0 besucht wird, gefolgt von seinen Nachbarn 1, 4 und 5, dann von den Nachbarn von 1 (3 und 4) und schließlich von dem Nachbarn von 3 (2).
