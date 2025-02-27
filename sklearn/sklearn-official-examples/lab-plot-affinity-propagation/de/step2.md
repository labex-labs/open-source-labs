# Generieren von Beispiel-Daten

Wir werden ein Beispiel-Datensatz mit der Funktion `make_blobs` aus dem Modul `sklearn.datasets` generieren. Die Funktion `make_blobs` erzeugt einen Datensatz von Punkten im n-dimensionalen Raum, wobei jeder Punkt zu einem der k Cluster gehört. Wir werden einen Datensatz mit 300 Punkten im 2-dimensionalen Raum generieren, mit 3 Clustern und einer Standardabweichung von 0,5.

```python
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)
```
