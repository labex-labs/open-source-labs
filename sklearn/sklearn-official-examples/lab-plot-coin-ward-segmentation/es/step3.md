# Calcular el agrupamiento

Con los datos y la matriz de conectividad definidos, ahora podemos realizar el agrupamiento jerárquico. Usaremos la clase `AgglomerativeClustering` de scikit-learn para realizar el agrupamiento. Estableceremos el número de clusters en 27, que es el número de monedas en la imagen. Usaremos el método de enlace "ward", que minimiza la varianza de las distancias entre los clusters que se están fusionando. También pasaremos la matriz de conectividad que creamos en el paso 2.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("Compute structured hierarchical clustering...")
st = time.time()
n_clusters = 27  # número de regiones
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"Elapsed time: {time.time() - st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {np.unique(label).size}")
```
