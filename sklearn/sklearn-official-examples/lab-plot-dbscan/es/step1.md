# Generación de datos

Usaremos la función make_blobs del módulo sklearn.datasets para generar un conjunto de datos sintéticos con tres clusters. El conjunto de datos constará de 750 muestras con una desviación estándar de cluster de 0.4. También estandarizaremos los datos usando el StandardScaler del módulo sklearn.preprocessing.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
