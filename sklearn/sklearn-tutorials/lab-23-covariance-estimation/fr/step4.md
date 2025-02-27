# Covariance inverse sparse

L'estimation de la covariance inverse sparse, également connue sous le nom de sélection de covariance, vise à estimer une matrice de précision sparse, où l'inverse de la matrice de covariance représente la matrice de corrélation partielle. Le package `sklearn.covariance` inclut une classe `GraphicalLasso` pour estimer la matrice de covariance inverse sparse en utilisant une pénalité l1.

```python
from sklearn.covariance import GraphicalLasso

# Crée un objet GraphicalLasso et l'ajuste aux données
graphical_lasso = GraphicalLasso().fit(data)

# Calcule la matrice de covariance inverse sparse
sparse_inverse_covariance_matrix = graphical_lasso.precision_
```
