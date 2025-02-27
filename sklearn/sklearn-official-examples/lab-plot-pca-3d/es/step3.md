# Realizar el PCA

A continuación, realizaremos el PCA en nuestro conjunto de datos. Primero concatenamos `x`, `y` y `z` para formar una matriz tridimensional `Y`. Luego creamos una instancia de la clase PCA y la ajustamos a nuestros datos. A continuación, podemos acceder a los componentes principales utilizando el atributo `components_` del objeto PCA.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
