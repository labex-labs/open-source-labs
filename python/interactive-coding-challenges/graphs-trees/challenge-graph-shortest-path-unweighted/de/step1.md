# Ungewichteter Graphkürzester Pfad

## Problemstellung

Gegeben ein gerichteter Graph ohne Kantengewichte, finde den kürzesten Pfad zwischen zwei Knoten.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Der Graph ist gerichtet.
- Der Graph ist ungewichtet.
- Die Klassen `Graph` und `Node` sind bereits verfügbar.
- Die Eingaben sind zwei Knoten.
- Die Ausgabe ist eine Liste von Knotenschlüsseln, die den kürzesten Pfad bilden.
- Wenn es keinen Pfad gibt, gebe `None` zurück.
- Der Graph ist zusammenhängend.
- Die Eingaben sind gültig.
- Der Algorithmus muss in den Speicher passen.

## Beispielverwendung

Angenommen, wir haben folgenden Graph:

```
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
```

Wir können den kürzesten Pfad zwischen zwei Knoten mit der Funktion `search_path` finden:

- `search_path(start=0, end=2) -> [0, 1, 3, 2]`
- `search_path(start=0, end=0) -> [0]`
- `search_path(start=4, end=5) -> None`
