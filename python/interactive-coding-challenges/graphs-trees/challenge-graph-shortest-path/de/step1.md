# Kürzester Pfad in einem Graphen

## Problemstellung

Gegeben ein gerichteter Graph mit gewichteten Kanten, finde den kürzesten Pfad zwischen zwei Knoten.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Ist dies ein gerichteter Graph? - Ja
- Könnte der Graph Zyklen enthalten? - Ja
  - Hinweis: Wenn die Antwort "nein" wäre, wäre dies ein DAG.
    - DAGs können mit einer [topologischen Sortierung](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/) gelöst werden.
- Sind die Kanten gewichtet? - Ja
  - Hinweis: Wenn die Kanten nicht gewichtet wären, könnten wir eine BFS durchführen.
- Sind alle Kanten nicht-negative Zahlen? - Ja
  - Hinweis: Graphen mit negativen Kanten können mit Bellman-Ford gelöst werden.
    - Graphen mit negativen Kostenzyklen haben keinen definierten kürzesten Pfad.
- Müssen wir auf nicht-negative Kanten prüfen? - Nein
- Können wir annehmen, dass dies ein zusammenhängender Graph ist? - Ja
- Können wir annehmen, dass die Eingaben gültig sind? - Nein
- Können wir annehmen, dass wir bereits eine Graph-Klasse haben? - Ja
- Können wir annehmen, dass wir bereits eine Prioritätswarteschlange-Klasse haben? - Ja
- Können wir annehmen, dass dies in den Speicher passt? - Ja

## Beispiel

Betrachte folgenden Graphen:

```txt
graph.add_edge('a', 'b', weight=5)
graph.add_edge('a', 'c', weight=3)
graph.add_edge('a', 'e', weight=2)
graph.add_edge('b', 'd', weight=2)
graph.add_edge('c', 'b', weight=1)
graph.add_edge('c', 'd', weight=1)
graph.add_edge('d', 'a', weight=1)
graph.add_edge('d', 'g', weight=2)
graph.add_edge('d', 'h', weight=1)
graph.add_edge('e', 'a', weight=1)
graph.add_edge('e', 'h', weight=4)
graph.add_edge('e', 'i', weight=7)
graph.add_edge('f', 'b', weight=3)
graph.add_edge('f', 'g', weight=1)
graph.add_edge('g', 'c', weight=3)
graph.add_edge('g', 'i', weight=2)
graph.add_edge('h', 'c', weight=2)
graph.add_edge('h', 'f', weight=2)
graph.add_edge('h', 'g', weight=2)
```

Wir können den kürzesten Pfad zwischen Knoten 'a' und Knoten 'i' mit der ShortestPath-Klasse finden:

```txt
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
```

Das erwartete Ergebnis ist:

```txt
['a', 'c', 'd', 'g', 'i']
```

Wir können auch das Gewicht des kürzesten Pfads überprüfen:

```txt
self.assertEqual(shortest_path.path_weight['i'], 8)
```
