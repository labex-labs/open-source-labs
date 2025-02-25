# Graph Dfs

## Problem

Implementiere die Tiefensuche (Depth-First Search, DFS) auf einem gerichteten Graphen. Der Algorithmus sollte an einem angegebenen Knoten beginnen und alle erreichbaren Knoten im Graphen besuchen. Die Reihenfolge, in der die Knoten besucht werden, sollte aufgezeichnet und als Liste zurückgegeben werden.

## Anforderungen

Um die Tiefensuche auf einem gerichteten Graphen zu implementieren, müssen die folgenden Anforderungen erfüllt werden:

- Der Graph ist gerichtet.
- Die Klassen Graph und Node sind bereits implementiert.
- Der Graph ist zusammenhängend.
- Die Eingaben sind gültig.
- Der Algorithmus passt in den Speicher.

## Beispielverwendung

Angenommen, wir haben einen gerichteten Graphen mit den folgenden Kanten:

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

Wenn wir die Tiefensuche bei Knoten 0 starten, sollte die Reihenfolge der besuchten Knoten [0, 1, 3, 2, 4, 5] sein.
