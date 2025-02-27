# Isomap

L'algorithme Isomap est l'un des premiers approches d'apprentissage sur variété. Il cherche une projection à basse dimension qui conserve les distances géodésiques entre tous les points.

```python
from sklearn.manifold import Isomap

# Crée une instance de l'algorithme Isomap
isomap = Isomap(n_components=2)

# Ajuste l'algorithme aux données et transforme les données dans l'espace à basse dimension
X_transformed = isomap.fit_transform(X)
```
