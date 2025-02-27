# Clustering berechnen

Mit den definierten Daten und der Verbindungsmatrix können wir jetzt hierarchisches Clustering durchführen. Wir werden die `AgglomerativeClustering`-Klasse von scikit-learn verwenden, um das Clustering durchzuführen. Wir werden die Anzahl der Cluster auf 27 setzen, was die Anzahl der Münzen im Bild ist. Wir werden die "ward"-Verknüpfungsmethode verwenden, die die Varianz der Distanzen zwischen den zu fusionierenden Clustern minimiert. Wir werden auch die Verbindungsmatrix übergeben, die wir im Schritt 2 erstellt haben.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # Anzahl der Regionen
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
