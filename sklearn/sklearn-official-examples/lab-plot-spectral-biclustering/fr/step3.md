# Ajuster `SpectralBiclustering`

Nous ajustons le modèle et comparons les clusters obtenus avec la vérité terrain. Notez que lors de la création du modèle, nous spécifions le même nombre de clusters que celui que nous avons utilisé pour créer l'ensemble de données (`n_clusters = (4, 3)`), ce qui contribuera à obtenir un bon résultat.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Calculer la similarité de deux ensembles de biclusters
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"consensus score: {score:.1f}")
```
