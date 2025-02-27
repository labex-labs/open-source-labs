# t-distributed Stochastic Neighbor Embedding (t-SNE)

Le t-SNE est une méthode populaire d'apprentissage sur variété qui convertit les affinités entre les points de données en probabilités. Il est particulièrement efficace pour visualiser les données à haute dimension.

```python
from sklearn.manifold import TSNE

# Crée une instance de l'algorithme t-SNE
tsne = TSNE(n_components=2)

# Ajuste l'algorithme aux données et transforme les données dans l'espace à basse dimension
X_transformed = tsne.fit_transform(X)
```
