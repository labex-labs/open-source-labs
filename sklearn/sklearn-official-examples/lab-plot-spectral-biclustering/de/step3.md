# Anpassen von `SpectralBiclustering`

Wir passen das Modell an und vergleichen die erhaltenen Cluster mit der wahren Klasse. Beachten Sie, dass wir bei der Erstellung des Modells die gleiche Anzahl von Clustern angeben, die wir verwendet haben, um den Datensatz zu erstellen (`n_clusters = (4, 3)`), was dazu beiträgt, ein gutes Ergebnis zu erzielen.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Berechnen der Ähnlichkeit zweier Mengen von Biclustern
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"Konsenswert: {score:.1f}")
```
