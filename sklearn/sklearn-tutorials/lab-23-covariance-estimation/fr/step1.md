# Covariance empirique

La matrice de covariance empirique est une méthode couramment utilisée pour estimer la matrice de covariance d'un ensemble de données. Elle est basée sur le principe de l'estimation du maximum de vraisemblance et suppose que les observations sont indépendantes et identiquement distribuées (i.i.d.). La fonction `empirical_covariance` du package `sklearn.covariance` peut être utilisée pour calculer la matrice de covariance empirique d'un ensemble de données donné.

```python
from sklearn.covariance import empirical_covariance

# Calcule la matrice de covariance empirique
covariance_matrix = empirical_covariance(data)
```
