# Ajustar `SpectralBiclustering`

Ajustamos el modelo y comparamos los clusters obtenidos con la verdad básica. Tenga en cuenta que al crear el modelo especificamos la misma cantidad de clusters que usamos para crear el conjunto de datos (`n_clusters = (4, 3)`), lo que contribuirá a obtener un buen resultado.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Compute the similarity of two sets of biclusters
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"consensus score: {score:.1f}")
```
