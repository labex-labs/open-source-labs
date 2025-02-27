# Rétrécissement Ledoit-Wolf

La méthode de rétrécissement Ledoit-Wolf fournit un coefficient de rétrécissement optimal qui minimise l'erreur quadratique moyenne entre la matrice de covariance estimée et la matrice de covariance réelle. Le package `sklearn.covariance` inclut une fonction `ledoit_wolf` qui peut être utilisée pour calculer l'estimateur Ledoit-Wolf pour un ensemble de données donné.

```python
from sklearn.covariance import ledoit_wolf

# Calcule l'estimateur Ledoit-Wolf de la matrice de covariance
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
