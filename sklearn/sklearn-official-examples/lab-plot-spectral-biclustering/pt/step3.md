# Ajustar `SpectralBiclustering`

Ajustamos o modelo e comparamos os clusters obtidos com a verdade fundamental. Note que, ao criar o modelo, especificamos o mesmo número de clusters que usamos para criar o conjunto de dados (`n_clusters = (4, 3)`), o que contribuirá para obter um bom resultado.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Calcular a similaridade de dois conjuntos de biclusters
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"score de consenso: {score:.1f}")
```
