# Estimer la matrice de covariance robuste

Dans cette étape, nous estimons une matrice de covariance robuste de l'ensemble de données en utilisant l'estimateur Minimum Covariance Determinant (MCD).

```python
# Estimate a robust covariance matrix of the dataset
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
