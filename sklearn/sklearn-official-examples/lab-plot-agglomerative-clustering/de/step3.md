# Erstellen eines Graphen

Erstellen Sie einen Graphen, der die lokale Konnektivität erfasst. Ein größerer Anzahl von Nachbarn liefert homogenere Cluster, allerdings auf Kosten der Rechenzeit. Eine sehr große Anzahl von Nachbarn liefert Clustergrößen, die gleichmäßiger verteilt sind, kann jedoch die lokale Mannigfaltigkeitsstruktur der Daten nicht erzwingen.

```python
knn_graph = kneighbors_graph(X, 30, include_self=False)
```
