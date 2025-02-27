# Isomap

El algoritmo Isomap es uno de los primeros enfoques para el aprendizaje de variedades. Busca una incrustación de baja dimensión que mantenga las distancias geodésicas entre todos los puntos.

```python
from sklearn.manifold import Isomap

# Crea una instancia del algoritmo Isomap
isomap = Isomap(n_components=2)

# Ajusta el algoritmo a los datos y transforma los datos al espacio de baja dimensión
X_transformed = isomap.fit_transform(X)
```
