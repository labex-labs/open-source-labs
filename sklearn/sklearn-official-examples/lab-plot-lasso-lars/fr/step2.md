# Calculer le chemin de Lasso

Ensuite, nous calculons le chemin de Lasso à l'aide de l'algorithme LARS. La fonction `lars_path` du module `linear_model` de Scikit-Learn est utilisée pour calculer le chemin de Lasso. La fonction prend les caractéristiques d'entrée, la variable cible et la méthode en tant que paramètres. Dans ce cas, nous utilisons la méthode "lasso" pour la régularisation L1.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
