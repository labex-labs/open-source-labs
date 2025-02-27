# Embedding Localmente Lineal (LLE)

El Embedding Localmente Lineal (LLE) es otro algoritmo de aprendizaje de variedades. Busca una proyección de baja dimensión de los datos que conserve las distancias dentro de los vecindarios locales.

```python
from sklearn.manifold import LocallyLinearEmbedding

# Crea una instancia del algoritmo LLE
lle = LocallyLinearEmbedding(n_components=2)

# Ajusta el algoritmo a los datos y transforma los datos al espacio de baja dimensión
X_transformed = lle.fit_transform(X)
```
