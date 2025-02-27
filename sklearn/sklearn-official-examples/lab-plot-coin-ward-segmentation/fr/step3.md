# Calculer l'agglomération

Avec les données et la matrice de connectivité définies, nous pouvons maintenant effectuer une agglomération hiérarchique. Nous utiliserons la classe `AgglomerativeClustering` de scikit-learn pour effectuer l'agglomération. Nous définirons le nombre de clusters à 27, qui est le nombre de pièces dans l'image. Nous utiliserons la méthode de liaison "ward", qui minimise la variance des distances entre les clusters en cours de fusion. Nous passerons également la matrice de connectivité que nous avons créée dans l'étape 2.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # nombre de régions
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
