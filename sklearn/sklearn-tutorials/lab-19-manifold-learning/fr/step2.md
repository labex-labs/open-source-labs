# Embedding localement linéaire (Locally Linear Embedding - LLE)

L'Embedding localement linéaire (LLE) est un autre algorithme d'apprentissage sur variété. Il cherche une projection à basse dimension des données qui conserve les distances au sein des voisinages locaux.

```python
from sklearn.manifold import LocallyLinearEmbedding

# Crée une instance de l'algorithme LLE
lle = LocallyLinearEmbedding(n_components=2)

# Ajuste l'algorithme aux données et transforme les données dans l'espace à basse dimension
X_transformed = lle.fit_transform(X)
```
