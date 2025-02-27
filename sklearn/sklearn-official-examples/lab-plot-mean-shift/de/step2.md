# Generieren von Stichprobendaten

Als nächstes werden wir Stichprobendaten mit der Funktion `make_blobs` aus dem Modul `sklearn.datasets` generieren. Wir werden einen Datensatz mit 10.000 Stichproben und drei Clustern mit Mittelpunkten bei `[[1, 1], [-1, -1], [1, -1]]` und einer Standardabweichung von 0,6 erstellen.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
```
