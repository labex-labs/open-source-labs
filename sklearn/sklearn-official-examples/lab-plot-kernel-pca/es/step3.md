# Usar PCA para proyectar el conjunto de datos

El PCA se utiliza para proyectar el conjunto de datos en un nuevo espacio que conserva la mayor parte de su variación original.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
