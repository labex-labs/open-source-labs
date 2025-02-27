# Realizar el PCA

Ahora que hemos visualizado el conjunto de datos, realicemos el PCA sobre él. Utilizaremos la función `PCA()` de scikit-learn para esto. Estableceremos el número de componentes en 3, ya que queremos reducir el conjunto de datos de 4 dimensiones (4 características) a 3 dimensiones.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
